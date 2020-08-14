import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.media_pb2 import Video

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

f = open("data/example.mp4", "rb")
video = f.read()
f.close()

datapoint = Datapoint(
    stream="test.video",
    video=Video(raw=video, duration=30000, mime_type="video/mp4"),
    timestamp=int(time.time() * 1000),
)

agent.PostData(datapoint)
