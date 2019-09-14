import json
import os
import sys
import time

from six.moves.urllib.request import Request, urlopen

host = "localhost"

data = {
    "stream": "test.text.http",
    "timestamp": int(time.time() * 1000),
    "text": {
        "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    },
    "tags": {
        "Region": "Europe"
    }
}
req = Request("http://%s:5502/v1/data" % host)
req.add_header("Content-Type", "application/json")
urlopen(req, json.dumps(data).encode("utf-8"))
