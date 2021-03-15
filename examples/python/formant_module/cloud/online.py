import datetime

from formant.sdk.cloud.v1 import Client as FormantCloudClient


def iso_seconds_ago(seconds):
    return (
        datetime.datetime.now(tz=datetime.timezone.utc)
        - datetime.timedelta(seconds=seconds)
    ).isoformat()


if __name__ == "__main__":
    fclient = FormantCloudClient()

    deviceId = "c04ca692-57f4-438d-8946-7b1e8b17e815"
    online_threshold_seconds = 10

    results = fclient.query(
        {
            "deviceIds": [deviceId],
            "names": ["$.agent.health"],
            "start": iso_seconds_ago(online_threshold_seconds),
            "end": iso_seconds_ago(0),
        }
    )

    if len(results) == 0:
        print("Not online.")
    else:
        print("Online.")
