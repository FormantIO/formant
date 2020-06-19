import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1 import datapoint_pb2, text_pb2

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

text = text_pb2.Text()
text.value = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
data_point = datapoint_pb2.Datapoint(
    stream="test.text.grpc",
    text=text,
    timestamp=int(time.time() * 1000),
    tags={"Region": "NorthAmerica"},
)
agent.PostData(data_point)
