# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import agent_pb2 as agent__pb2


class AgentStub(object):
  """gRPC service for the Figure Agent
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StreamData = channel.stream_unary(
        '/agent.Agent/StreamData',
        request_serializer=agent__pb2.Datapoint.SerializeToString,
        response_deserializer=agent__pb2.StreamDataResponse.FromString,
        )
    self.PostData = channel.unary_unary(
        '/agent.Agent/PostData',
        request_serializer=agent__pb2.Datapoint.SerializeToString,
        response_deserializer=agent__pb2.PostDataResponse.FromString,
        )
    self.RegisterROSTopic = channel.unary_unary(
        '/agent.Agent/RegisterROSTopic',
        request_serializer=agent__pb2.ROSTopic.SerializeToString,
        response_deserializer=agent__pb2.RegisterROSTopicResponse.FromString,
        )
    self.GetROSTopics = channel.unary_unary(
        '/agent.Agent/GetROSTopics',
        request_serializer=agent__pb2.GetROSTopicsRequest.SerializeToString,
        response_deserializer=agent__pb2.GetROSTopicsResponse.FromString,
        )


class AgentServicer(object):
  """gRPC service for the Figure Agent
  """

  def StreamData(self, request_iterator, context):
    """Accepts a stream of data points.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostData(self, request, context):
    """Accepts a single data point per RPC call. Also exposed as a HTTP Endpoint.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterROSTopic(self, request, context):
    """Registers a ROS Topic and its msg type.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetROSTopics(self, request, context):
    """Gets the ROS topics defined in the agent config.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StreamData': grpc.stream_unary_rpc_method_handler(
          servicer.StreamData,
          request_deserializer=agent__pb2.Datapoint.FromString,
          response_serializer=agent__pb2.StreamDataResponse.SerializeToString,
      ),
      'PostData': grpc.unary_unary_rpc_method_handler(
          servicer.PostData,
          request_deserializer=agent__pb2.Datapoint.FromString,
          response_serializer=agent__pb2.PostDataResponse.SerializeToString,
      ),
      'RegisterROSTopic': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterROSTopic,
          request_deserializer=agent__pb2.ROSTopic.FromString,
          response_serializer=agent__pb2.RegisterROSTopicResponse.SerializeToString,
      ),
      'GetROSTopics': grpc.unary_unary_rpc_method_handler(
          servicer.GetROSTopics,
          request_deserializer=agent__pb2.GetROSTopicsRequest.FromString,
          response_serializer=agent__pb2.GetROSTopicsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'agent.Agent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
