import os
import time

import grpc

from protos.agent.v1 import agent_pb2, agent_pb2_grpc
from protos.model.v1 import commands_pb2, datapoint_pb2, math_pb2, text_pb2

import subprocess

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

request = agent_pb2.GetCommandRequestRequest()
command = agent.GetCommandRequest(request)

def generate_datapoint(arg):
    numeric_msg = math_pb2.Numeric()
    numeric_msg.value = float(arg) * 2
    return datapoint_pb2.Datapoint(stream="command.numeric.result",
                                   numeric=numeric_msg,
                                   timestamp=int(time.time() * 1000))

if command.request.id != "":
    print("Received command request:\n%s" % command)

    if command.request.command == "my_command":
        # example command which ingests a numeric datapoint
        # equal to twice the input value
        response = commands_pb2.CommandResponse(
            datapoint=generate_datapoint(command.request.text),
            request_id=command.request.id)
        response.success = True
    else:
        text = text_pb2.Text()
        text.value = "command not supported"
        datapoint = datapoint_pb2.Datapoint(stream="command.error",
                                            text=text,
                                            timestamp=int(time.time() * 1000))
        response = commands_pb2.CommandResponse(
            datapoint=datapoint,
            request_id=command.request.id)
        response.success = False

    request = agent_pb2.SendCommandResponseRequest(response=response)
    agent.SendCommandResponse(request)
    print("Sent command response\n%s" % request)
else:
    print("No pending command requests found.")
