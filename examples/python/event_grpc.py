import time

import grpc

from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc

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
