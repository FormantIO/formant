import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.media_pb2 import Image

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

f = open("../../data/cargo.png", "rb")
image = f.read()
f.close()

datapoint = Datapoint(
    stream="test.image",
    image=Image(raw=image, content_type="image/png"),
    timestamp=int(time.time() * 1000),
)

agent.PostData(datapoint)
