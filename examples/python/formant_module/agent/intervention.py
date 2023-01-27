import os
from formant.sdk.agent.v1 import Client

fclient = Client()
title = "Identify Color"
instruction = "Select the color of the pallet in the picker."
options = ["Pink", "White", "Orange", "Blue"]
hint = 0
content_type = "image/png"
path = os.path.dirname(os.path.realpath(__file__))
url = "%s/../../../data/picker.png" % path
response = fclient.create_selection_intervention_request(
    title, instruction, options, hint, url, content_type
)
id = response.id
request_response = fclient.get_intervention_response(id)
print(request_response.selection_response.value)
