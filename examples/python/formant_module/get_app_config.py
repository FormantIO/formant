import time
import random
from formant.sdk.agent.v1 import Client as FormantClient


if __name__ == "__main__":
    fclient = FormantClient()

    low_power_mode = fclient.get_app_config("low_power_mode", None) == "true"

    if low_power_mode:
        print("Entering low power mode.")

    cycle_period = 1.0 if low_power_mode else 0.25

    while True:
        fclient.post_numeric("example.numeric", random.random())
        time.sleep(cycle_period)
