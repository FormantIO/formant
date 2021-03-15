from typing import Optional
import os
import sys
import time
import uuid
import subprocess

from formant.sdk.agent.v1 import Client as FormantClient


COMMAND_SCRIPT_MAPPING = {
    "start_software": "/path/to/script",
    "stop_software": "...",
    "restart_software": "...",
    "activate_tests": "...",
    "start_recording": "...",
    "stop_recording": "...",
}


class SearchableTestAdapter:
    def __init__(self):
        self.id = None  # type: Optional[str]
        self.start_timestamp = None  # type: Optional[int]
        self.software_version = None  # type: Optional[str]
        self.log_level = None  # type: Optional[str]
        self.is_shutdown = False  # type: bool

        self.fclient = FormantClient(ignore_unavailable=True)

        # listen for commands
        self.fclient.register_command_request_callback(
            self.issue_command, command_filter=COMMAND_SCRIPT_MAPPING.keys()
        )

        # listen for changes to Formant application configuration
        self.update_app_config()
        self.fclient.register_config_update_callback(self.update_app_config)

        # idly spin while the command request callback listens for commands
        while not self.is_shutdown:
            time.sleep(1.0)

    def __del__(self):
        self.is_shutdown = True

    def update_app_config(self):
        self.software_version = self.fclient.get_app_config(
            "software_version", None
        )  # add defaults in place of None
        self.log_level = self.fclient.get_app_config("log_level", None)

    def reset_session(self):
        # Searchable session events via uuid naming scheme, e.g. "R473b9f9ada91"
        self.id = "R" + "".join(str(uuid.uuid4()).split("-")[0:2])
        self.start_time = 1000 * int(time.time())

    def run_script(self, path):
        if os.path.exists(path):
            subprocess.run("bash " + path, shell=True, check=True)

    def issue_command(self, request):
        if request.command == "start_recording":
            self.reset_session()
        elif (
            request.command == "stop_recording"
            and self.id is not None
            and self.start_time is not None
        ):
            self.fclient.create_event(
                self.id + ": Recording session",
                timestamp=self.start_time,
                end_timestamp=1000 * int(time.time()),
            )
            self.id = None
            self.start_time = None

        success = True
        try:
            self.run_script(COMMAND_SCRIPT_MAPPING.get(request.command))
        except Exception:
            success = False

        self.fclient.send_command_response(request.id, success=success)


if __name__ == "__main__":
    try:
        SearchableTestAdapter()
    except KeyboardInterrupt:
        sys.exit()
