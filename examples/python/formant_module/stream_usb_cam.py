import sys
import cv2
from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True)

    cap = cv2.VideoCapture(0)  # usb cam may be on a different index: try 1, 2 ...
    if cap is None:
        sys.exit()

    while True:
        _, image = cap.read()
        encoded = cv2.imencode(".jpg", image)[1].tostring()
        fclient.post_image("usb_cam", encoded)
