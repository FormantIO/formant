import time

from formant.sdk.agent.v1 import Client as FormantClient

POINT_STREAM_NAME = "video.click"


def handle_mouse_click(control_datapoint):
    point = control_datapoint.point
    print(point.x)  # [0,1] from top left
    print(point.y)  # [0,1] from top left
    print(point.z)  # 0


if __name__ == "__main__":
    fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True)
    fclient.register_teleop_callback(
        handle_mouse_click, stream_filter=[POINT_STREAM_NAME]
    )

    while True:
        time.sleep(10)
