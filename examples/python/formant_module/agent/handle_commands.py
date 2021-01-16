import subprocess
import time

from formant.sdk.agent.v1 import Client as FormantClient

SENSOR_ADDRESSES = ["192.168.1.28, 192.168.1.29"]
MOTOR_ADDRESSES = ["192.168.30.90", "192.168.30.91", "192.168.30.92", "192.168.30.93"]

fclient = FormantClient()


def ping(address):
    # check if the address responds within 0.1 seconds
    shell_command = ["timeout", "0.1", "ping", "-c", "1", address]
    try:
        subprocess.check_output(shell_command)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


def handle_command_request(request):
    if request.command == "sensor_check":
        addresses = SENSOR_ADDRESSES
    elif request.command == "motor_check":
        addresses = MOTOR_ADDRESSES
    else:
        return

    success = not (False in list(map(ping, addresses)))
    fclient.send_command_response(request.id, success=success)


if __name__ == "__main__":
    fclient.register_command_request_callback(
        handle_command_request, command_filter=["sensor_check", "motor_check"]
    )

    # idly spin while the command request callback listens for commands
    while True:
        time.sleep(0.1)
