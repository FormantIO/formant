#!/usr/bin/env python

from __future__ import absolute_import, print_function

import os
import time

import grpc
import roslib
import rospy
import rostopic
import tf2_ros
import toml

from protos.agent.v1 import agent_pb2, agent_pb2_grpc
from protos.model.v1 import datapoint_pb2, ros_pb2

try:
    from cStringIO import StringIO  # Python 2.x
except ImportError:
    from io import StringIO  # Python 3.x


class BridgeNode(object):
    """A ROS node that forwards ROS topics to the Formant Agent.
    
    This node will:
    - Subscribe to ROS topics specified in the Agent configuration file
    - Register the ROS message descriptions of these topics with the Agent
    - Forward all received messages in their serialized wire format to the Agent
    """

    def __init__(self):
        self._subscribers = []
        self._include_transform = {}
        self._agent_server_cert = None
        self._configure()
        self._setup_agent_communication()
        # setup tf2 listener
        self._tf_buffer = tf2_ros.Buffer()
        self._tf_listener = tf2_ros.TransformListener(self._tf_buffer)

    def _configure(self):
        """Reads the Formant Agent configuration file."""

        # The location of the configuration file depends on whether the agent was
        # installed locally or via debian package.
        try:
            home = os.path.expanduser("~")
            config = toml.load('%s/.formant/config.toml' % home)
        except:
            config = toml.load('/home/formant/config.toml')

        self.agent_address = "%s:%s" % (
            config['formant']['agent-server-ip'],
            config['formant']['agent-server-port-grpc'])

        # Experimental -- use the agent's certificate for secure gRPC communication
        if 'agent-server-cert' in config['formant']:
            self._agent_server_cert = config['formant']['agent-server-cert']
            if self._agent_server_cert:
                if not os.path.isfile(self._agent_server_cert):
                    print("Server certificate does not exist or is unreadable.")

    def _setup_agent_communication(self):
        """Creates a gRPC stub for communication with the Formant Agent."""
        if self._agent_server_cert:
            creds = grpc.ssl_channel_credentials(
                open(self._agent_server_cert).read())
            self.channel = grpc.secure_channel(self.agent_address, creds)
        else:
            self.channel = grpc.insecure_channel(self.agent_address)

        self.channel.subscribe(
            self._handle_connectivity_change, try_to_connect=True)
        self.agent_stub = agent_pb2_grpc.AgentStub(self.channel)

    def _handle_connectivity_change(self, connectivity):
        """Handle changes to gRPC channel connectivity."""
        if connectivity == grpc.ChannelConnectivity.READY:
            response = self.agent_stub.GetROSWorldReferenceFrameID(
                agent_pb2.GetROSWorldReferenceFrameIDRequest())
            self._world_reference_frame_id = response.world_reference_frame_id
            response = self.agent_stub.GetROSTopicsSubscriptionConfig(
                agent_pb2.GetROSTopicsSubscriptionConfigRequest())
            for topic_config in (response.topics):
                self._include_transform[topic_config.
                                        topic] = topic_config.include_transform
            self._subscribe_to_topics(
                [topic_config.topic for topic_config in response.topics])
            print("Agent communication established.")
        if connectivity == grpc.ChannelConnectivity.SHUTDOWN:
            # In the case of shutdown, re-establish the connection from scratch
            self._setup_agent_communication()

    def _subscribe_to_topics(self, topics):
        """Subscribes to a list of topics."""
        self._unsubscribe_all()

        topics = set(topics)
        all_topics = set([topic[0] for topic in rospy.get_published_topics()])
        for topic in (topics - all_topics):
            print("Cannot subscribe to %s; not in the ROS runtime." % topic)

        for topic in (topics & all_topics):
            data_type = rostopic.get_topic_type(topic, blocking=False)[0]
            if not data_type:
                print("Cannot subscribe to %s; no data type found." % topic)
                continue

            message_class = roslib.message.get_message_class(data_type)
            if not message_class:
                print("Cannot subscribe to %s; no message class found." % topic)
                continue

            message_description = message_class._full_text
            if not message_description:
                print("Cannot subscribe to %s; no message description found." %
                      topic)

            self._subscribe(topic, str(data_type), message_class,
                            message_description)

    def _subscribe(self, topic_name, data_type, message_class, msg_desc):
        """Subscribes to a topic and registers its message description with the Agent."""
        if not self.agent_stub:
            print(
                "Cannot subscribe to %s; no agent stub to register message description with."
                % topic_name)
            return
        self.agent_stub.RegisterROSTopic(
            ros_pb2.ROSTopic(
                name=topic_name, data_type=data_type, msg_desc=msg_desc))

        self._subscribers.append(
            rospy.Subscriber(
                topic_name,
                message_class,
                callback=self._handle_message,
                callback_args=topic_name,
                queue_size=10))

    def _unsubscribe_all(self):
        """Unsubscribes from all topics."""
        for sub in self._subscribers:
            sub.unregister()
        self._subscribers = []

    def _handle_message(self, msg, topic_name):
        """Handles arrival of a new ROS message."""
        if not self.agent_stub:
            print("Cannot handle message from %s; no agent stub." % topic_name)
            return

        # Take the timestamp from the message header if present,
        # otherwise use the current time
        local_frame_id = ""
        timestamp = int(time.time() * 1000)
        if hasattr(msg, 'header'):
            header_timestamp = (
                msg.header.stamp.secs * 1000 + msg.header.stamp.nsecs / 1000000)
            # sanity check to make sure ros header stamp is in epoch time
            if header_timestamp > 1500000000000:
                timestamp = header_timestamp
            stamp = msg.header.stamp
            local_frame_id = msg.header.frame_id
        # Embed the ROS message in a gRPC message and send it to the Agent.
        ros_msg_data = ros_pb2.ROSMessage()
        buffer = StringIO()
        msg.serialize(buffer)
        ros_msg_data.raw = buffer.getvalue()
        # if transform required include it
        if self._include_transform[topic_name] and local_frame_id:
            try:
                transform_stamped = self._tf_buffer.lookup_transform(
                    self._world_reference_frame_id, local_frame_id, stamp)
                buffer = StringIO()

                transform_stamped.transform.serialize(buffer)
                ros_msg_data.world_to_local = buffer.getvalue()
            except Exception as e:
                print(
                    "Error getting transform for %s with world_reference_frame_id=%s and local_reference_frame_id=%s"
                    % (topic_name, self._world_reference_frame_id,
                       local_frame_id))
                print(e)
                return
        datapoint = datapoint_pb2.Datapoint(
            stream=topic_name, ros_message=ros_msg_data, timestamp=timestamp)
        try:
            self.agent_stub.PostData(datapoint)
        except grpc.RpcError as e:
            print("Exception handling message from %s" % topic_name)
            print(e)
