import datetime

from formant.sdk.cloud.v1 import Client as FormantClient


def get_current_isodate():
    return datetime.datetime.now(tz=datetime.timezone.utc).isoformat()


if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()

    device_id = "43be1d4b-2178-46b8-81b5-61cf865e264b"

    print("Sending command ...")
    command_result = fclient.create_command(
        {
            "deviceId": device_id,
            "command": "start_recording",
            "parameter": {"scrubberTime": get_current_isodate()},
        }
    )
    print(command_result)
    print("\n")

    print("requesting on demand data")
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    yesterday = now - datetime.timedelta(days=1)

    on_demand_result = fclient.demand_device_data(device_id, now, yesterday)
    print(on_demand_result)
    print("\n")

    # file id obtained by uploading to formant file storage
    # see files.py for an example
    file_id = "ffcd8958-6f94-4b0d-b9a9-3cbf105c3df5"

    print("Sending command with large payload ...")
    command_result = fclient.create_command(
        {
            "deviceId": device_id,
            "command": "snapshot",
            "parameter": {
                "scrubberTime": get_current_isodate(),
                "files": [{"id": file_id, "name": "view_0.jpg"}],
            },
        }
    )

    print(command_result)
    print("\n")

    print("Querying for device's currently undelivered commands ...")
    query_commands_result = fclient.query_commands({"deviceId": device_id})
    print(query_commands_result)
