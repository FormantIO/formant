import rospy
from geometry_msgs.msg import Twist, TwistStamped
from std_msgs.msg import Header

SUBSCRIBER_TOPIC = "/cmd_vel"
PUBLISHER_TOPIC = "/cmd_vel_stamped"


class TwistStamper:
    def __init__(self):
        self._subscriber = rospy.Subscriber(
            SUBSCRIBER_TOPIC, Twist, self._twist_callback
        )
        self._publisher = rospy.Publisher(PUBLISHER_TOPIC, TwistStamped)

    def _twist_callback(self, twist):
        header = Header(stamp=rospy.Time.now())
        msg_stamped = TwistStamped(header=header, twist=twist)
        self._publisher.publish(msg_stamped)


rospy.init_node("twist_stamper")
TwistStamper()
rospy.spin()
