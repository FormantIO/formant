import time

from formant.sdk.agent.v1 import Client as FormantClient

DIRECTORY = "/path/to/file/"
VIDEO_STREAM_NAME = "vid"


def handle_telemetry(datapoint):
    try:
        with open("%svideo%s.mp4" % (DIRECTORY, time.time()), "xb") as wfile:
            wfile.write(datapoint.datapoint.video.raw)
    except FileExistsError as e:
        print(e)


if __name__ == "__main__":
    fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True)
    fclient.register_telemetry_listener_callback(
        handle_telemetry, stream_filter=[VIDEO_STREAM_NAME]
    )

    while True:
        time.sleep(10)
