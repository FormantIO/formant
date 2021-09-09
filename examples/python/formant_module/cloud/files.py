import datetime

from formant.sdk.cloud.v1 import Client as FormantClient


if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient(
        admin_api="http://localhost:8080",
    )

    print("Uploading file ...")
    result = fclient.upload_file(
        {
            "path": "/tmp/test.log",
        }
    )
    print(result)
