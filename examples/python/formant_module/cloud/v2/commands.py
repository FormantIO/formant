import datetime

from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.commands import (
    Command,
    CommandParameter,
    CommandParameterMeta,
    FileInfo,
    CommandQuery,
)


FORMANT_REQUEST_ON_DEMAND_DATA_COMMAND_NAME = "formant.demand_data"


def get_current_isodate():
    return datetime.datetime.now(tz=datetime.timezone.utc)


def get_timestamp_str(
    dt,  # type: datetime.datetime
):
    return str(int(dt.timestamp()))


if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()
    admin_api = fclient.admin

    device_id = "58d7f6e1-899d-4a8a-8c02-4c805cc8227f"
    command = "start_recording"
    command_parameter = CommandParameter(scrubber_time=get_current_isodate())
    command = Command(
        device_id=device_id,
        command=command,
        parameter=command_parameter,
        organization_id=fclient.admin.organization_id,
    )

    print("Sending command ...")
    response = admin_api.commands.create(command)
    command_result = response.parsed
    print(command_result)
    print("\n")

    # This needs to be reviewed
    print("requesting on demand data")
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    yesterday = now - datetime.timedelta(days=1)
    command_parameter_meta = CommandParameterMeta()
    command_parameter_meta.additional_properties = {
        "start": get_timestamp_str(now),
        "end": get_timestamp_str(yesterday),
    }
    command_parameter = CommandParameter(
        meta=command_parameter_meta, scrubber_time=get_current_isodate()
    )
    command = Command(
        device_id=device_id,
        organization_id=admin_api.organization_id,
        command=FORMANT_REQUEST_ON_DEMAND_DATA_COMMAND_NAME,
        parameter=command_parameter,
    )
    response = admin_api.commands.create(command)
    on_demand_result = response.parsed
    print(on_demand_result)
    print("\n")

    # file id obtained by uploading to formant file storage
    # see files.py for an example
    file_id = "751d52af-0771-446d-9962-83ddd65f04bc"
    files = [FileInfo(id=file_id, name="view_0.jpg")]
    command_parameter = CommandParameter(
        scrubber_time=get_current_isodate(), files=files
    )
    command = Command(
        device_id=device_id,
        command="snapshot",
        parameter=command_parameter,
        organization_id=admin_api.organization_id,
    )

    print("Sending command with large payload ...")

    response = admin_api.commands.create(command)
    command_result = response.parsed
    print(command_result)
    print("\n")

    command_query = CommandQuery(device_id=device_id)

    print("Querying for device's currently undelivered commands ...")
    response = admin_api.commands.query(command_query)
    query_commands_result = response.parsed
    print(query_commands_result)
