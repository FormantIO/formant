import json
import os
import time

from six.moves.urllib.request import Request, urlopen

path = os.path.dirname(os.path.realpath(__file__))
host = "localhost"

data = {
    "event": {
        "timestamp": int(time.time() * 1000),
        "message": "Synchronized transporter annular confinement beam to warp frequency 0.72e-17 hz",
        "notification_enabled": True,
        "tags": {"Region": "South"},
    }
}
req = Request("http://%s:5502/v1/events" % host)
req.add_header("Content-Type", "application/json")
response = urlopen(req, json.dumps(data).encode("utf-8"))
response_body = response.read()
response_json = json.loads(response_body)
print("Created event %s" % response_json)
