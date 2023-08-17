from formant.sdk.agent.v1 import Client as FormantClient


def main():
    fclient = FormantClient()
    # Make an API call with agent authentication
    result = fclient.call_cloud(
                "https://api.formant.io/v1/admin/streams/",
                "GET",
                body="",
                headers={"Content-Type": "application/json"},
                require_formant_auth=True,
                buffer_call=False,
                is_retryable=False,
                retryable_status_codes=[-1] # Default retry behavior
                )

    # A result is only returned when buffer_call is set to False
    print(result.statusCode)
    print(result.responseBody)


if __name__ == "__main__":
    main()
