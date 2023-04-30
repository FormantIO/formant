import json
import os
import sys
import time
import random

from six.moves.urllib.request import Request, urlopen

host = "localhost"

# create an array of 100 random points

names = []
pos = []
vel = []
eff = []

spot_names = [
  "fl.hx",
  "fl.hy",
  "fl.kn",
  "fr.hx",
  "fr.hy",
  "fr.kn",
  "hl.hx",
  "hl.hy",
  "hl.kn",
  "hr.hx",
  "hr.hy",
  "hr.kn",
  "arm0.sh0",
  "arm0.sh1",
  "arm0.hr0",
  "arm0.el0",
  "arm0.wr0",
  "arm0.wr1",
  "arm0.wr2",
  "arm0.eff",
  "arm0.eff_gripper0",
  "arm0.eff_gripper1"
]

num_names = len(spot_names)

for i in range(0, num_names):
    names.append(spot_names[i])
    pos.append(random.random())
    vel.append(random.random())
    eff.append(random.random())


jsonData = json.dumps({ 
    "name": names,
    "position": pos,
    "velocity": vel,
    "effort": eff
})

data = {
    "stream": "joints.json",
    "timestamp": int(time.time() * 1000),
    "json": {
        "value": jsonData
    }
}
req = Request("http://%s:5502/v1/data" % host)
req.add_header("Content-Type", "application/json")
urlopen(req, json.dumps(data).encode("utf-8"))
