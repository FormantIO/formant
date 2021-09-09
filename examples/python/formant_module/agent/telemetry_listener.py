import time
import random

from formant.sdk.agent.v1 import Client as FormantClient


def handle_telemetry(datapoint):
    print("Received datapoint:", datapoint)


if __name__ == "__main__":
    fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True)

    # Handling data ...
    fclient.register_telemetry_listener_callback(
        handle_telemetry, stream_filter=["example.numeric", "example.numericset"]
    )

    # Post datapoints with varying types at varying intervals...
    while True:
        time.sleep(random.random() / 10.0)  # wait 0.0 to 0.1 seconds between datapoints

        r = random.random()
        if r < 0.33:
            print("post numeric")
            fclient.post_numeric("example.numeric", r)
        elif r < 0.66:
            print("post text")
            fclient.post_text(
                "example.text", "This text datapoint is ignored by the stream filter"
            )
        else:
            print("post numericset")
            fclient.post_numericset(
                "example.numericset",
                {"Height": (random.random(), "m"), "Width": (random.random(), "m")},
            )

