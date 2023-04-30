import json
import os
import sys
import time
import random

from six.moves.urllib.request import Request, urlopen

host = "localhost"

# create an array of 100 random points

pos = []
col = []
for i in range(0, 100):
    pos.append(random.random())
    pos.append(random.random())
    pos.append(random.random())
    col.append(random.random())
    col.append(random.random())
    col.append(random.random())
    col.append(1.0)



jsonData = json.dumps({ 
    "pcd":{
        "positions": pos,
        "colors": col
    }
})

data = {
    "stream": "point_cloud.json",
    "timestamp": int(time.time() * 1000),
    "json": {
        "value": jsonData
    }
}
req = Request("http://%s:5502/v1/data" % host)
req.add_header("Content-Type", "application/json")
urlopen(req, json.dumps(data).encode("utf-8"))
