import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1 import datapoint_pb2, navigation_pb2

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

geo = navigation_pb2.Location()
geo.latitude = 37.8199
geo.longitude = -122.4783
geo_datapoint = datapoint_pb2.Datapoint(
    stream="test.gps", location=geo, timestamp=int(time.time() * 1000)
)
response = agent.PostData(geo_datapoint)
