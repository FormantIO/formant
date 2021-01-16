from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient()

    query_result = fclient.query(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "tags": {"location": ["sf"]},
        }
    )
    print(query_result)
