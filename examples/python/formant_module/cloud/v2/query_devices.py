from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.devices import DeviceQuery

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    fclient = FormantClient()
    admin_api = fclient.admin

    device_query = DeviceQuery(tags={"location": ["sf"]})
    response = admin_api.devices.query(device_query)
    result = response.parsed
    print(result)
