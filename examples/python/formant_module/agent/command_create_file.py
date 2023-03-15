import datetime
import time
import os

from formant.sdk.agent.v1 import Client as FormantClient


fclient = FormantClient()
# Folder for Formant directory watch
HOME_DIR = os.path.expanduser("~")
DIR_TO_WATCH = os.path.join(HOME_DIR, "watch_me")


def handle_command_request(request):
    # How to get the command's parameters and timestamp
    command_text = request.text
    command_time = datetime.datetime.fromtimestamp(request.scrubber_time.seconds)

    # Create a file with data from the command in the watched directory
    out_file_path = os.path.join(DIR_TO_WATCH, command_text + ".txt")
    output_text = f"Command received:\n{command_text}\nat time:\n{command_time}\n"
    print(output_text)
    with open(out_file_path, "w") as f:
        f.write(output_text)


if __name__ == "__main__":
    fclient.register_command_request_callback(
        handle_command_request, command_filter=["echo_to_file"]
    )

    # idly spin while the command request callback listens for commands
    while True:
        time.sleep(0.1)

