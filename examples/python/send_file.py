import os
import time

import grpc

from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1 import datapoint_pb2, file_pb2

path = os.path.dirname(os.path.realpath(__file__))
channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

file_datapoint = file_pb2.File()
file_path = "%s/data/planets.csv" % path
file_datapoint.url = file_path
file_datapoint.filename = "planets.csv"
request = datapoint_pb2.Datapoint(
    stream="test.file", file=file_datapoint, timestamp=int(time.time() * 1000)
)
agent.PostData(request)
