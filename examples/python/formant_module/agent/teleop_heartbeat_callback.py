import time

from formant.sdk.agent.v1 import Client as FormantAgentClient


def f(heartbeat):
    print("Received heartbeat callback at", time.time())
    print(heartbeat.is_disconnect)


if __name__ == "__main__":
    fclient = FormantAgentClient(ignore_unavailable=True)
    fclient.register_teleop_heartbeat_callback(f)

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        exit()
