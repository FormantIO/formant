import json
import os
import sys
import time

from six.moves.urllib.request import Request, urlopen

host = "localhost"

jsonData = json.dumps({ 
    "orderNumber": 1000,
    "items": [
        {
            "name": "Veggie Burrito",
            "unit_price": 7.55,
            "quantity": 2
        },
        {
            "name": "+Chicken (Burrito)",
            "unit_price": 1.99,
            "quantity": 4
        },
        {
            "name": "Guacamole (Side)",
            "unit_price": 5.99,
            "quantity": 1
        }
    ]
})

data = {
    "stream": "test.json.http",
    "timestamp": int(time.time() * 1000),
    "json": {
        "value": jsonData
    },
    "tags": {
        "Region": "Cartlandia"
    }
}
req = Request("http://%s:5502/v1/data" % host)
req.add_header("Content-Type", "application/json")
urlopen(req, json.dumps(data).encode("utf-8"))
