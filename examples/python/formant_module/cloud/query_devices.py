from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()

    result = fclient.query_devices({"tags": {"location": "sf"}})
    print(result)
