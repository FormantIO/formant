#!/usr/bin/env python

from __future__ import absolute_import, print_function

import base64
import json
import time
import urllib2
from multiprocessing import Queue
from os.path import expanduser

import grpc

import agent_pb2
import agent_pb2_grpc


def create_data_point(point):
    timestamp = int(time.time() * 1000)
    text_msg = agent_pb2.Text()
    text_msg.value = 'this is a python %s data point' % point
    data_point = agent_pb2.Datapoint(
        stream="stream.001", text=text_msg, timestamp=timestamp)
    print('created datapoint:\n%s' % str(data_point))
    return data_point


def write_datapoints():
    while agent_stub is not None:
        yield create_data_point("stream")
        time.sleep(10)


def post_data():
    agent_stub.PostData(create_data_point("posted"))


def http_post_data():
    data = {
        'stream': "stream.001",
        'timestamp': int(time.time() * 1000),
        'text': {'value': 'this is a python http posted data point'}
    }
    req = urllib2.Request('http://localhost:5502/v1/data')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    print("http post response %s" % response.code)


def stream_data():
    agent_stub.StreamData(write_datapoints())


channel = grpc.insecure_channel("localhost:5501")
agent_stub = agent_pb2_grpc.AgentStub(channel)
print('agent comm established.')
http_post_data()
# sleep for 200ms to avoid throttling.
time.sleep(0.2)
post_data()
# sleep for 200ms to avoid throttling.
time.sleep(0.2)
stream_data()
