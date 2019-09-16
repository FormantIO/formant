import os
import random
import time

import grpc

from protos.agent.v1 import agent_pb2_grpc
from protos.model.v1 import datapoint_pb2, math_pb2

path = os.path.dirname(os.path.realpath(__file__))
channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

numeric_msg = math_pb2.Numeric()
numeric_msg.value = random.uniform(0, 1)
data_point = datapoint_pb2.Datapoint(stream="test.numeric",
                                     numeric=numeric_msg,
                                     timestamp=int(time.time() * 1000))
agent.PostData(data_point)
