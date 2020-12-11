import os
import time

import grpc

from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc
from formant.protos.model.v1 import intervention_pb2, event_pb2

path = os.path.dirname(os.path.realpath(__file__))
channel = grpc.insecure_channel("localhost:5501")
agent_stub = agent_pb2_grpc.AgentStub(channel)

request = intervention_pb2.InterventionRequest()
request.timestamp = int(time.time() * 1000)
request.severity = event_pb2.INFO
request.selection_request.title = "Identify Color"
request.selection_request.hint = 1
request.selection_request.instruction = "Select the color of the pallet in the picker."
request.selection_request.image.content_type = "image/png"
request.selection_request.image.url = "%s/../../data/picker.png" % path
request.selection_request.options.extend(["Pink", "White", "Orange", "Blue"])
create_response = agent_stub.CreateInterventionRequest(request)
print("Created intervention request %s" % create_response)

print("Waiting for intervention response")
response_request = agent_pb2.GetInterventionResponseRequest()
response_request.request_id = create_response.id
response_response = agent_stub.GetInterventionResponse(response_request)
print("Received intervention response %s" % response_response)
