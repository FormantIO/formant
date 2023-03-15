import datetime

from formant.sdk.cloud.v2 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()
    admin_api = fclient.admin

    print("Uploading file ...")
    result = admin_api.files.upload(path="/tmp/tesa.log")
    print(result)
