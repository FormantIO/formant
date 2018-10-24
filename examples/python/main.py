#!/usr/bin/env python

from __future__ import absolute_import, print_function

import base64
import json
import sys
import time
import urllib2

import grpc

import agent_pb2
import agent_pb2_grpc

#### gRPC Implementations ####

def create_data_point(point):
    timestamp = int(time.time() * 1000)
    text_msg = agent_pb2.Text()
    text_msg.value = 'this is a %s data point' % point
    data_point = agent_pb2.Datapoint(
        stream="stream.001", text=text_msg, timestamp=timestamp)
    return data_point


def write_datapoints():
    while agent_stub is not None:
        yield create_data_point("stream")
        time.sleep(10)


def post_data():
    agent_stub.PostData(create_data_point("posted"))


def stream_data():
    agent_stub.StreamData(write_datapoints())

def upload_file(path):
    file_datapoint = agent_pb2.File()
    file_datapoint.url = "file://%s/fruit-single.png" % path
    request = agent_pb2.Datapoint(
        stream = "file.log", file = file_datapoint, timestamp = int(time.time() * 1000)
    )
    agent_stub.PostData(request)


def post_geolocation():
    geo = agent_pb2.Location()
    geo.latitude = 37.434417
    geo.longitude = -122.142925
    geo_datapoint = agent_pb2.Datapoint(
        stream = "geo.001", location = geo, timestamp = int(time.time() * 1000)
    )
    agent_stub.PostData(geo_datapoint)

def create_intervention_request(path):
    request = agent_pb2.InterventionRequest()
    request.timestamp = int(time.time() * 1000)
    request.severity = agent_pb2.INFO
    request.selection_request.hint = 1
    request.selection_request.instruction = "What is in the image?"
    request.selection_request.image.content_type = "image/png"
    request.selection_request.image.url = "file://%s/fruit-single.png" % path
    request.selection_request.options.extend(
        ["option 1",
         "option 2",
         "option 3"
         ])
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
        'text': {'value': 'this is a python http posted data point'}
    }
    req = urllib2.Request('http://localhost:5502/v1/data')
    req.add_header('Content-Type', 'application/json')
    return urllib2.urlopen(req, json.dumps(data))

def create_intervention_request_http(path):
    data = {
        'severity': "INFO",
        'timestamp': int(time.time() * 1000),
        "selection_request": {
            "hint": 1,
            "image": {
                "content-type": "image/png",
                "url": ("file://%s/fruit-single.png" % path)
            },
            "options": [
                "option 1",
                "option 2",
                "option 3"
            ],
            "instruction": "What is in the image?"
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
    print('\n#################################################################################\n')


#### Datapoints ####

# Need path for file uploads and intervention requests
path = sys.argv[1]
channel = grpc.insecure_channel("localhost:5501")
agent_stub = agent_pb2_grpc.AgentStub(channel)
print('agent comm established.')

print_example_break()

print('posting data grpc')
post_data()
time.sleep(0.2)

print_example_break()

print('posting geo location')
post_geolocation()
time.sleep(0.2)

print_example_break()

print('posting local file')
upload_file(path)

print_example_break()
print('posting data http')
post_data_http()
time.sleep(0.2)

print_example_break()

#### InterventionRequests ####

print('creating intervention request')
request = create_intervention_request(path)
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
request = create_intervention_request_http(path)
print(request)
request_id_http = request.get("id")
time.sleep(1)

print_example_break()

print('getting intervention request http')
print(get_intervention_request_http(request_id_http))
time.sleep(1)

print_example_break()

print('getting intervention response http')
# this will wait for you to respond in the #all channel
print(get_intervention_response_http(request_id_http))

print_example_break()

#### Datapoint Streaming ####
time.sleep(10)
print('streaming datapoints\nuse ctrl+c to exit')
# stream data
stream_data()
