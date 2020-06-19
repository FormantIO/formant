import json
import os
import time

import grpc

from protos.agent.v1 import agent_pb2_grpc
from protos.model.v1 import datapoint_pb2, text_pb2

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

jsonData = json.dumps({
  "_id": "5ed956785df9ea8693924e90",
  "index": 0,
  "guid": "aa4989e7-9fd2-487d-a977-9eb8f722e3e3",
  "isActive": True,
  "balance": "$3,858.05",
  "picture": "http://placehold.it/32x32",
  "age": 23,
  "eyeColor": "green",
  "name": {
    "first": "Potter",
    "last": "Espinoza"
  },
  "company": "KRAG",
  "email": "potter.espinoza@krag.org",
  "phone": "+1 (888) 492-2071",
  "address": "976 Herkimer Street, Wedgewood, Louisiana, 186",
  "about": "Consectetur nostrud ex consectetur duis. Enim cupidatat veniam aliquip consectetur est occaecat enim anim reprehenderit qui proident esse consequat. Cupidatat sit qui aliquip sunt ullamco aliquip veniam officia. Nulla incididunt aliquip officia voluptate nulla laborum esse fugiat voluptate.",
  "registered": "Sunday, May 20, 2018 1:49 AM",
  "latitude": "16.917591",
  "longitude": "149.179144",
  "tags": [
    "quis",
    "esse",
    "Lorem",
    "deserunt",
    "sunt"
  ],
  "friends": [
    {
      "id": 0,
      "name": "Castillo Huffman"
    },
    {
      "id": 1,
      "name": "Martha Montoya"
    },
    {
      "id": 2,
      "name": "Taylor Foley"
    }
  ],
  "greeting": "Hello, Potter! You have 8 unread messages.",
  "favoriteFruit": "strawberry"
})

json = text_pb2.Json()
json.value = jsonData
data_point = datapoint_pb2.Datapoint(stream="test.json.grpc",
                                     json=json,
                                     timestamp=int(time.time() * 1000),
                                     tags={"Region": "Laurelhurst"})
agent.PostData(data_point)
