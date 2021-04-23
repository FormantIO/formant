from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()

    device_id = "572f5ff3-63e9-4687-b242-c0d8a4891d80"

    # query by tags
    query_result = fclient.query(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "tags": {"location": ["sf"]},
        }
    )

    # query by device
    query_result = fclient.query(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "deviceIds": [device_id],
        }
    )
    print(query_result)
