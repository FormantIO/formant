import os
import random
import time

import grpc

from grpc_status import rpc_status
from protos.agent.v1 import agent_pb2, agent_pb2_grpc
from protos.model.v1 import datapoint_pb2, math_pb2

path = os.path.dirname(os.path.realpath(__file__))
channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

datapoints = []
for x in range(0, 20):
    numeric_msg = math_pb2.Numeric()
    numeric_msg.value = random.uniform(0, 1)
    data_point = datapoint_pb2.Datapoint(stream="test.numeric",
                                         numeric=numeric_msg,
                                         timestamp=int(time.time() * 1000))
    datapoints.append(data_point)
    # force some throttling errors to see error handling
    time.sleep(.001)

request = agent_pb2.PostDataMultiRequest(datapoints=datapoints)

try:
    agent.PostDataMulti(request)
# catch rpcError
except grpc.RpcError as e:
    status = rpc_status.from_call(e)
    for post_data_multi_error in status.details:
        if post_data_multi_error.Is(agent_pb2.PostDataMultiError.DESCRIPTOR):
            # unpack error details into proto agent_pb2.PostDataMultiError
            post_data_multi_error_pb = agent_pb2.PostDataMultiError()
            post_data_multi_error.Unpack(post_data_multi_error_pb)
            for error in post_data_multi_error_pb.errors:
                # iterate through errors and check for retryable
                if error.retryable:
                    print("datapoint at index %s is retryable" % error.index)
                else:
                    print("datapoint at index %s is not retryable" % error.index)
