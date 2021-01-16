import time

from formant.sdk.agent.v1 import Client as FormantClient


def handle_teleop(control_datapoint):
    if control_datapoint.stream == "Joystick":
        handle_joystick(control_datapoint)
    elif control_datapoint.stream == "Localization":
        handle_destination(control_datapoint)
    elif control_datapoint.stream == "Buttons":
        handle_buttons(control_datapoint)


def handle_joystick(_):
    print(_.stream)
    print(_.timestamp)
    print(_.twist.linear.x)
    print(_.twist.angular.z)


def handle_destination(_):
    print(_.stream)
    print(_.timestamp)
    print(_.pose.translation.x)
    print(_.pose.rotation.w)


def handle_buttons(_):
    print(_.stream)
    print(_.timestamp)
    print(_.bitset.bits)


if __name__ == "__main__":
    fclient = FormantClient(ignore_throttled=True, ignore_unavailable=True,)

    # Handling data ...
    fclient.register_teleop_callback(
        handle_teleop, ["Joystick", "Localization", "Buttons"]
    )

    # Sending data ...
    while True:
        fclient.post_bitset(
            "Status",
            {
                "PTZ mode": True,
                "Walk mode": False,
                "Has lease": True,
                "Has estop": False,
                "FLIR online": True,
            },
        )
        time.sleep(0.05)
