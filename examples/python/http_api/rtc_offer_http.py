import json
import os
import time

from six.moves.urllib.request import Request, urlopen

path = os.path.dirname(os.path.realpath(__file__))
host = "localhost"

data = {"offer_sdp": "asdf"}
req = Request("http://%s:5502/v1/rtc-offer" % host)
req.add_header("Content-Type", "application/json")
response = urlopen(req, json.dumps(data).encode("utf-8"))
response_body = response.read()
response_json = json.loads(response_body)
print("RTC offer %s" % response_json)
