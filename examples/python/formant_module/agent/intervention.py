import os
import time
from formant.sdk.agent.v1 import Client as FormantClient


# The image that is displayed with the request
# (use a local file for the purpose of example)
IMAGE_PATH = os.path.join(os.getcwd(), "example_image.png")
IMAGE_TYPE = "image/png"
SEVERITY_TYPE = "info"

fclient = FormantClient()

def selection_request():
    print("Sending selection intervention request")
    response = fclient.create_selection_intervention_request(
        title="Identify Color",
        instruction="What color is the big robot?",
        options=["Pink", "White", "Orange", "Blue"],
        hint=0,
        url=IMAGE_PATH,
        content_type=IMAGE_TYPE,
        severity=SEVERITY_TYPE
    )
    response_id = response.id

    # Optionally ingest the link to the intervention request, which can be used
    # as an event trigger
    url = "app.formant.io/events/%s" % response_id
    fclient.post_text("intervention_url", url)

    intervention_response = fclient.get_intervention_response(response_id)
    print("Selection received:\n%s" % intervention_response.selection_response.value)

def labeling_request():
    print("Sending labeling intervention request")
    response = fclient.create_labeling_intervention_request(
        title="Locate and Label Object",
        instruction="Draw a box around the big robot and select its type.",
        labels={"Label1": "Sweeper", "Label2": "Mover"},
        url=IMAGE_PATH,
        content_type=IMAGE_TYPE,
        severity=SEVERITY_TYPE
    )
    response_id = response.id

    url = "app.formant.io/events/%s" % response_id
    fclient.post_text("intervention_url", url)

    intervention_response = fclient.get_intervention_response(response_id)
    print("Labeling received:\n%s" % intervention_response.labeling_response.value)


if __name__ == "__main__":
    selection_request()
    time.sleep(5)
    labeling_request()
