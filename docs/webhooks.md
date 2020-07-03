Webhooks allow arbitrary endpoints to subscribe to real-time Formant events.

All triggered events will route to each configured webhook.

The Formant cloud will send POST requests with a JSON body to the provided webhooks.

For reference, here is a simple flask server that processes Formant events.

```python
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def formant_event():
    event = request.get_json()
    print(event["payload"]["message"])
    print(event["payload"]["value"])
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

Example payload:

```json
{
    "eventType": "alert",
    "payload": {
        "id": "e0be1601-0ac2-41f8-b239-1dbe9a2d68db",
        "message": "Oven temperature high",
        "severity": "warning",
        "streamName": "oven.temperature_c",
        "streamType": "numeric",
        "tags": {
            "location": "sf"
        },
        "value": 250,
        "time": "2019-03-09T00:13:22.903Z",
        "deviceId": "c281e95e-c8f1-41b4-b573-e9138eab8900",
        "sourceUrl": "https://app.formant.io/events/e0be1601-0ac2-41f8-b239-1dbe9a2d68db"
    }
}
```
