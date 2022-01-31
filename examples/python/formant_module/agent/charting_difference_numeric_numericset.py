import random

import rospy
from geometry_msgs.msg import Twist, Vector3
from formant.sdk.agent.v1 import Client as FormantAgentClient
from formant.sdk.agent.v1.exceptions import Throttled


"""
This examples charts a ROS twist in two different ways
to demonstrate the different charting options in Formant.

If neither of these charting methods is suitable for you,
you can always make a custom module with the toolkit.
https://github.com/FormantIO/toolkit
"""


def continually_publish_twists(pub):
    """
    Continuously publish random Twist messages to the /cmd_vel topic.
    """
    while rospy.is_shutdown() is False:
        pub.publish(
            Twist(
                linear=Vector3(x=random.random(), y=random.random(), z=random.random()),
                angular=Vector3(
                    x=random.random(), y=random.random(), z=random.random()
                ),
            )
        )
        rospy.sleep(0.1)  # publish at 10hz


if __name__ == "__main__":
    rospy.init_node("adapter_example")

    # Dealing with throttling:
    # 1. add ignore_throttled to client instantiation
    # 2. catch `Throttled` exceptions (imported above) on the `post_numeric` or `post_numericset` methods
    fclient = FormantAgentClient(ignore_throttled=True)

    def callback(msg):
        print("Received: {}".format(msg))

        # Two charting methods shown below:

        # 1. Use a numeric set
        fclient.post_numericset(
            "cmd_vel",
            {
                "linear.x": (msg.linear.x, "m/s"),  # numeric sets include units
                "linear.y": (msg.linear.y, "m/s"),
                "linear.z": (msg.linear.z, "m/s"),
                "angular.x": (msg.angular.x, "m/s"),
                "angular.y": (msg.angular.y, "m/s"),
                "angular.z": (msg.angular.z, "m/s"),
            },
        )

        # 2. Use tags to define different lines in a stacked chart.
        fclient.post_numeric("cmd_vel.linear", msg.linear.x, tags={"linear": "x"})
        fclient.post_numeric("cmd_vel.linear", msg.linear.y, tags={"linear": "y"})
        fclient.post_numeric("cmd_vel.linear", msg.linear.z, tags={"linear": "z"})

        fclient.post_numeric("cmd_vel.angular", msg.angular.x, tags={"angular": "x"})
        fclient.post_numeric("cmd_vel.angular", msg.angular.y, tags={"angular": "y"})
        fclient.post_numeric("cmd_vel.angular", msg.angular.z, tags={"angular": "z"})

        # 3. Create a custom view to create a custom visualization for any JSON data
        # see https://github.com/FormantIO/toolkit

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    rospy.Subscriber("/cmd_vel", Twist, callback)

    continually_publish_twists(pub)
