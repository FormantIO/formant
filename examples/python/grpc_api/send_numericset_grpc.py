import os
import random
import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1 import datapoint_pb2, math_pb2

path = os.path.dirname(os.path.realpath(__file__))
channel = grpc.insecure_channel()
agent = agent_pb2_grpc.AgentStub(channel)

numericset_msg = math_pb2.NumericSet

numeric_msg1 = math_pb2.NumericSetEntry()
numeric_msg1.value = random.uniform(0, 1000)
numeric_msg1.label = "frequency"
numeric_msg1.unit = "Hz"

numericset_msg.Numerics.extend(numeric_msg1)

numeric_msg2 = math_pb2.NumericSetEntry()
numeric_msg2.value = random.uniform(0, 100)
numeric_msg2.label = "usage"
numeric_msg2.unit = "percent"

numericset_msg.Numerics.extend(numeric_msg2)

data_point = datapoint_pb2.Datapoint(
    stream="test.numeric_set",
    numeric_set=numericset_msg,
    timestamp=int(time.time() * 1000),
)
agent.PostData(data_point)
