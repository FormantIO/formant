import os
import subprocess
import time

import grpc

from protos.agent.v1 import agent_pb2, agent_pb2_grpc
from protos.model.v1 import commands_pb2, datapoint_pb2, file_pb2

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

request = agent_pb2.GetCommandRequestStreamRequest(command_filter=[])

for r in agent.GetCommandRequestStream(request):
    print("Received command request:\n%s" % r.request)
