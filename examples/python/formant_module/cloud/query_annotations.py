import datetime
from formant.sdk.cloud.v1 import Client as FormantClient
import json

DEVICE_ID = "b0990d5a-cdff-4c3c-ab71-c6c72be385ad"


def main():
    fclient = FormantClient()
    week_ago = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
        days=7
    )
    query_tags = {"Status": ["Succesful"]}
    annotations = fclient.query_annotations(week_ago, [DEVICE_ID], tags=query_tags)
    print(json.dumps(annotations, indent=1))


if __name__ == "__main__":
    main()
