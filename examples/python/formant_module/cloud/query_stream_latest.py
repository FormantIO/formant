from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()

    device_id = "572f5ff3-63e9-4687-b242-c0d8a4891d80"

    # query last known value of all streams from a device
    # within a given period
    query_result = fclient.query_stream_current_value(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "deviceIds": [device_id],
        }
    )
    print(query_result)

    # query last known value of all streams matching a name
    query_result = fclient.query_stream_current_value(
        {
            "names": ["engine_temp"],
        }
    )

    # query last known value of all streams matching a tag
    query_result = fclient.query_stream_current_value(
        {
            "tags": {"location": ["sf"]},
        }
    )
