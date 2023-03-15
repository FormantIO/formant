from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.stream_current import ScopeFilter
import dateutil.parser as parser

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()
    query_api = fclient.query

    # query last known value of all streams from a device
    # within a given period
    device_id = "58d7f6e1-899d-4a8a-8c02-4c805cc8227f"
    start = parser.isoparse("2021-01-01T00:00:00.000Z")
    end = parser.isoparse("2021-01-10T00:00:00.000Z")
    scope_filter = ScopeFilter(start=start, end=end, device_ids=[device_id])
    response = query_api.stream_current.query(scope_filter=scope_filter)
    query_result = response.parsed
    print(query_result)

    # query last known value of all streams matching a name
    scope_filter = ScopeFilter(names=["engine_temp"])
    response = query_api.stream_current.query(scope_filter=scope_filter)
    query_result = response.parsed
    print(query_result)

    # query last known value of all streams matching a tag
    scope_filter = ScopeFilter(tags={"location": ["sf"]})
    response = query_api.stream_current.query(scope_filter=scope_filter)
    query_result = response.parsed
    print(query_result)
