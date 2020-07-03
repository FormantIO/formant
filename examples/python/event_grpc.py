import os
import time

import grpc

from protos.agent.v1 import agent_pb2, agent_pb2_grpc
from protos.model.v1 import event_pb2

agent = agent_pb2_grpc.AgentStub(grpc.insecure_channel("localhost:5501"))
request = agent_pb2.CreateEventRequest()
request.event.timestamp = int(time.time() * 1000)
request.event.message = (
    "Synchronized transporter annular confinement beam to warp frequency 0.45e17 hz"
)
request.event.notification_enabled = True
request.event.tags["Region"] = "North"
response = agent.CreateEvent(request)
print("Created event %s" % response)
