#!/usr/bin/env python

from __future__ import absolute_import, print_function

import base64
import json
import os
import random
import sys
import time
import urllib2

import grpc

import agent_pb2
import agent_pb2_grpc

path = os.path.dirname(os.path.realpath(__file__))

#### gRPC Implementations ####


def create_data_point(point):
    timestamp = int(time.time() * 1000)
    text_msg = agent_pb2.Text()
    text_msg.value = 'this is a %s data point' % point
    data_point = agent_pb2.Datapoint(
        stream="stream.001.text", text=text_msg, timestamp=timestamp)
    return data_point


def create_numeric_data_point():
    timestamp = int(time.time() * 1000)
    numeric_msg = agent_pb2.Numeric()
    numeric_msg.value = random.uniform(0, 1)
    data_point = agent_pb2.Datapoint(
        stream="stream.001.numeric", numeric=numeric_msg, timestamp=timestamp)
    return data_point


def spam_datapoints():
    i = 0
    unthrottled_count = 0
    while agent_stub is not None and i < 100:
        print('spamming file and text datapoints')
        try:
            agent_stub.PostData(create_numeric_data_point())
            unthrottled_count += 1
        except grpc.RpcError as e:
            unthrottled_count -= 1
            print(e)
        print(unthrottled_count)
        time.sleep(0.005)
        i += 1


def write_datapoints():
    i = 0
    while agent_stub is not None and i < 10:
        point = create_data_point("stream")
        print_example_break()
        print("streaming datapoint:\n %s" % point)
        print_example_break()
        yield point
        time.sleep(0.2)
        i += 1


def post_data():
    try:
        agent_stub.PostData(create_data_point("posted"))
    except grpc.RpcError as e:
        print(e)


def stream_data():
    try:
        agent_stub.StreamData(write_datapoints())
    except grpc.RpcError as e:
        print(e)


def upload_file():
    file_datapoint = agent_pb2.File()
    file_path = "file://%s/fruit-single.png" % path
    file_datapoint.url = file_path
    request = agent_pb2.Datapoint(
        stream="file.log",
        file=file_datapoint,
        timestamp=int(time.time() * 1000))
    try:
        agent_stub.PostData(request)
    except grpc.RpcError as e:
        print(e)


def upload_data_file():
    file_datapoint = agent_pb2.File()
    file_path = "%s/fruit-single.png" % path
    with open(file_path, "rb") as f:
        data = f.read()
        file_datapoint.raw = data
        file_datapoint.filename = "testfile1"
        request = agent_pb2.Datapoint(
            stream="file.log",
            file=file_datapoint,
            timestamp=int(time.time() * 1000))
    try:
        agent_stub.PostData(request)
    except grpc.RpcError as e:
        print(e)


def post_geolocation():
    geo = agent_pb2.Location()
    geo.latitude = 37.434417
    geo.longitude = -122.142925
    geo_datapoint = agent_pb2.Datapoint(
        stream="geo.001", location=geo, timestamp=int(time.time() * 1000))
    try:
        agent_stub.PostData(geo_datapoint)
    except grpc.RpcError as e:
        print(e)


def create_intervention_request():
    request = agent_pb2.InterventionRequest()
    request.timestamp = int(time.time() * 1000)
    request.severity = agent_pb2.INFO
    request.selection_request.title = "Selection Request"
    request.selection_request.hint = 1
    request.selection_request.instruction = "What is in the image?"
    request.selection_request.image.content_type = "image/png"
    request.selection_request.image.url = "file://%s/fruit-single.png" % path
    request.selection_request.options.extend(
        ["option 1", "option 2", "option 3"])
    response = agent_stub.CreateInterventionRequest(request)
    return response


def get_intervention_request(id):
    request = agent_pb2.GetInterventionRequestRequest()
    request.id = id
    return agent_stub.GetInterventionRequest(request)


def get_intervention_response(id):
    response_request = agent_pb2.GetInterventionResponseRequest()
    response_request.request_id = id
    return agent_stub.GetInterventionResponse(response_request)


#### HTTP Implementations ####


def post_data_http():
    data = {
        'stream': "stream.001",
        'timestamp': int(time.time() * 1000),
        'text': {
            'value': 'this is a python http posted data point'
        }
    }
    req = urllib2.Request('http://localhost:5502/v1/data')
    req.add_header('Content-Type', 'application/json')
    return urllib2.urlopen(req, json.dumps(data))


def create_intervention_request_http():
    data = {
        'severity': "INFO",
        'timestamp': int(time.time() * 1000),
        "labeling_request": {
            "title":
            "Labeling Request",
            "image": {
                "content-type": "image/png",
                "url": ("file://%s/fruit-many.png" % path)
            },
            "instruction":
            "Select all the fruit.",
            "labels": [{
                "value": "53e3f75e-63a6-4e38-a19a-02893021be89",
                "display_name": "pear",
            }]
        }
    }
    req = urllib2.Request('http://localhost:5502/v1/intervention-requests')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    response_body = response.read()
    response_json = json.loads(response_body)
    return response_json


def get_intervention_request_http(id):
    req = urllib2.Request(
        'http://localhost:5502/v1/intervention-requests/%s' % id)
    response = urllib2.urlopen(req)
    response_body = response.read()
    response_json = json.loads(response_body)
    return response_json


def get_intervention_response_http(id):
    req = urllib2.Request(
        'http://localhost:5502/v1/intervention-responses/%s' % id)
    response = urllib2.urlopen(req)
    response_body = response.read()
    response_json = json.loads(response_body)
    return response_json


def print_example_break():
    print(
        '\n#################################################################################\n'
    )


#### Datapoints ####

channel = grpc.insecure_channel("localhost:5501")
agent_stub = agent_pb2_grpc.AgentStub(channel)
print('agent comm established.')

print('posting data grpc')
post_data()
time.sleep(0.2)

print_example_break()

print('posting geo location')
post_geolocation()
time.sleep(0.2)

print_example_break()

print('posting local file')
upload_file()

print_example_break()
print('posting data http')
post_data_http()
time.sleep(0.2)

print_example_break()

#### InterventionRequests ####

print('creating intervention request')
request = create_intervention_request()
print(request)
request_id = request.id
time.sleep(1)

print_example_break()

print('getting intervention request')
print(get_intervention_request(request_id))
time.sleep(1)

print_example_break()

print('getting intervention response')
# this will wait for you to respond in the #all channel
print(get_intervention_response(request_id))
time.sleep(1)

print_example_break()

print('creating intervention request http')
request = create_intervention_request_http()
print(json.dumps(request, indent=4))
request_id_http = request.get("id")
time.sleep(1)

print_example_break()

print('getting intervention request http')
print(json.dumps(get_intervention_request_http(request_id_http), indent=4))
time.sleep(1)

print_example_break()

print('getting intervention response http')
# this will wait for you to respond in the #all channel
print(json.dumps(get_intervention_response_http(request_id_http), indent=4))

print_example_break()

#### Datapoint Throttling ####
print('spamming datapoints')
time.sleep(3)
spam_datapoints()
print_example_break()

#### Datapoint Streaming ####
time.sleep(3)
print('streaming datapoints\nuse ctrl+c to exit')
time.sleep(2)
# stream data
stream_data()
