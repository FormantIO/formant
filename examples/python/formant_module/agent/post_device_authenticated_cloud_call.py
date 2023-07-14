from formant.sdk.agent.v1 import Client as FormantClient


def main():
    fclient = FormantClient()
    result = fclient.call_cloud(
                "https://api.formant.io/v1/admin/streams/",
                "GET",
                body="",
                headers={"Content-Type": "application/json"},
                require_formant_auth=True,
                buffer_call=True,
                is_retryable=True,
                retryable_status_codes=[403])
    print(result.statusCode)
    print(result.responseBody)


if __name__ == "__main__":
    main()
