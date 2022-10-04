import time
import threading
from formant.sdk.agent.v1 import Client as FormantAgentClient

NO_HEARTBEAT_DISCONNECTION_THRESHOLD = 0.1
current_timer = None


def trigger_disconnected():
    print("Disconnected")


def f(_):
    global current_timer
    if current_timer is not None:
        current_timer.cancel()
    print("Received heartbeat callback at", time.time())
    current_timer = threading.Timer(
        NO_HEARTBEAT_DISCONNECTION_THRESHOLD, trigger_disconnected
    )
    current_timer.start()


if __name__ == "__main__":
    fclient = FormantAgentClient(ignore_unavailable=True)
    fclient.register_teleop_heartbeat_callback(f)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        exit()
