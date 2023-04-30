import os
import time
from formant.sdk.agent.v1 import Client as FormantClient


IMAGE_PATH = os.path.join(os.getcwd(), "my_image.jpg")
IMAGE_TYPE = "image/jpg"
SEVERITY_TYPE = "warning"

fclient = FormantClient()

def selection_request():
    print("Sending selection intervention request")
    response = fclient.create_selection_intervention_request(
        title="Identify Color",
        instruction="Select the color of the pallet in the picker.",
        options=["Pink", "White", "Orange", "Blue"],
        hint=0,
        url=IMAGE_PATH,
        content_type=IMAGE_TYPE,
        severity=SEVERITY_TYPE
    )
    response_id = response.id
    intervention_response = fclient.get_intervention_response(response_id)
    print("Selection received:\n%s" % intervention_response.selection_response.value)

def labeling_request():
    print("Sending labeling intervention request")
    response = fclient.create_labeling_intervention_request(
        title="Locate and Label Object",
        instruction="Draw a box around the object and select its type.",
        labels={"Label1": "Label1Value", "Label2": "Label2Value"},
        url=IMAGE_PATH,
        content_type=IMAGE_TYPE,
        severity=SEVERITY_TYPE
    )
    response_id = response.id
    intervention_response = fclient.get_intervention_response(response_id)
    print("Labeling received:\n%s" % intervention_response.labeling_response.value)


if __name__ == "__main__":
    selection_request()
    time.sleep(5)
    labeling_request()
