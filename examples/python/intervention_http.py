import json
import os
import time

from six.moves.urllib.request import Request, urlopen

path = os.path.dirname(os.path.realpath(__file__))
host = "localhost"

data = {
    "severity": "INFO",
    "timestamp": int(time.time() * 1000),
    "labeling_request": {
        "title": "Select Inventory",
        "image": {"content-type": "image/png", "url": ("%s/data/cargo.png" % path)},
        "instruction": "Draw box around all cargo palettes",
        "labels": [
            {"value": "53e3f75e-63a6-4e38-a19a-02893021be89", "display_name": "Cargo",}
        ],
    },
}
req = Request("http://%s:5502/v1/intervention-requests" % host)
req.add_header("Content-Type", "application/json")
response = urlopen(req, json.dumps(data).encode("utf-8"))
response_body = response.read()
response_json = json.loads(response_body)
print("Created intervention request %s" % response_json)
id = response_json.get("id")

print("Waiting for intervention response")
req = Request("http://%s:5502/v1/intervention-responses/%s" % (host, id))
response = urlopen(req)
response_body = response.read()
response_json = json.loads(response_body)
print("Received intervention response %s" % response_json)
