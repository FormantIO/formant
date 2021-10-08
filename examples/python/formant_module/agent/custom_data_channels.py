import random
import time
import json

from formant.sdk.agent.v1 import Client as FormantAgentClient


def callback(message):
    print(json.loads(message))


if __name__ == "__main__":
    fclient = FormantAgentClient()
    fclient.register_custom_data_channel_message_callback(callback)

    def f():
        d = {
            "t": time.time(),
            "X": [random.random() for _ in range(10)],
        }
        payload = json.dumps(d).encode("utf-8")

        # To send and receive on custom data channels,
        # any channels ("test-sdk" in this case) must be created by your custom interface.

        # For instance,
        # using the Data SDK in the toolkit (https://github.com/FormantIO/toolkit):
        # `await device.createCustomDataChannel("test-sdk");`

        fclient.send_on_custom_data_channel("test-sdk", payload)

    while True:
        time.sleep(0.1)
        f()
