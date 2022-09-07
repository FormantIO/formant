import time
from geometry_msgs.msg import PoseStamped
from scipy.spatial.transform import Rotation

from formant.sdk.agent.v1 import Client as FormantClient


class FormantPositionCommander:
    def __init__(self):
        self._fclient = FormantClient(ignore_unavailable=True, ignore_throttled=True)
        self._setup_position_command_handler()

    def _setup_position_command_handler(self):
        self._fclient.register_command_request_callback(
            self._send_pose, command_filter=["send_to_position"]
        )

    def _send_pose(self, request):
        print("Parameters sent from command: %s" % request.text)
        try:
            position_data = request.text.split(",")
            x_pos = float(position_data[0])
            y_pos = float(position_data[1])
            theta = float(position_data[2])
            goal_position = PoseStamped()
            goal_position.pose.position.x = float(position_data[0])
            goal_position.pose.position.y = float(position_data[1])
            rot = Rotation.from_euler(
                "xyz", [0, 0, float(position_data[2])], degrees=True
            )
            rot_quat = rot.as_quat()
            goal_position.pose.orientation.x = rot_quat[0]
            goal_position.pose.orientation.y = rot_quat[1]
            goal_position.pose.orientation.z = rot_quat[2]
            goal_position.pose.orientation.w = rot_quat[3]
            print("Goal position: %s" % goal_position)
        except Exception as e:
            print(
                "Ensure you send command with x, y, and theta as comma separated values."
            )
            print("Data sent: %s" % request.text)


if __name__ == "__main__":
    FPC = FormantPositionCommander()
    while True:
        time.sleep(1)
