import time
from formant.sdk.agent.v1 import Client as FormantClient

toggle = True

if __name__ == "__main__":
    fclient = FormantClient(
        ignore_throttled=True,
        ignore_unavailable=True
    )

    # Toggles enabled status of API "testbtn" every second
    while True:
        print("toggling testbtn status")
        fclient.post_bitset(
            "Buttons",
            {
                "testbtn": toggle,
            },
        )
        time.sleep(1)
        toggle = not toggle
