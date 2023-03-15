import datetime

from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.queries import Query


def iso_seconds_ago(seconds):
    return datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
        seconds=seconds
    )


if __name__ == "__main__":
    fclient = FormantClient()
    query_api = fclient.query

    deviceId = "58d7f6e1-899d-4a8a-8c02-4c805cc8227f"
    online_threshold_seconds = 10

    query = Query(
        start=iso_seconds_ago(online_threshold_seconds),
        end=iso_seconds_ago(0),
        device_ids=[deviceId],
        names=["$.agent.health"],
    )
    response = query_api.queries.query(query)
    results = response.parsed

    if len(results.items) == 0:
        print("Not online.")
    else:
        print("Online.")
