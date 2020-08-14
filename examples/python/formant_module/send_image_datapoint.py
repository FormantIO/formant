import cv2
from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient()

    image = cv2.imread("/path/to/example.jpg")
    encoded = cv2.imencode(".jpg", image)[1].tostring()

    fclient.post_image("example.image", encoded)
