import datetime
from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.events import EventQuery

import json

DEVICE_ID = "58d7f6e1-899d-4a8a-8c02-4c805cc8227f"


def main():
    fclient = FormantClient()
    admin_api = fclient.admin
    week_ago = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
        days=7
    )
    query_tags = {"Status": ["Succesful"]}

    event_query = EventQuery(start=week_ago, device_ids=[DEVICE_ID], tags=query_tags)
    response = admin_api.events.query(event_query)
    annotations = response.parsed

    print(annotations)


if __name__ == "__main__":
    main()
