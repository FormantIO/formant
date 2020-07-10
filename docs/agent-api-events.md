### Sending custom events with the agent API

Before custom events can be sent from a device, the Formant agent must be installed, running, and provisioned on that device.

[Installing the agent](./agent-debian-install.md)

### What is a custom event?

Events are moments of interest experienced by a device that an organization can search for, navigate to and between, and receive notifications about. Custom events are a type of event that can be created programmatically via the agent API.

A custom event object is comprised of the following data:

```
// Time of occurence
timestamp

// Information about occurence
message

// Whether a notification should be emitted
notificationEnabled

// Optional associated stream name
streamName

// Optional associated stream type
streamType

// Optional key-value tags associated with event
tags
```

[See the event proto file for reference.](../protos/model/v1/event.proto)

### How do I create events from a device?

Call the `CreateEvent` API with a `CreateEventRequest` object to post an event to Formant. Here is an example of using the `CreateEvent` API to send event which notifies .

```python
import time

import grpc
from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc

agent = agent_pb2_grpc.AgentStub(grpc.insecure_channel("localhost:5501"))
request = agent_pb2.CreateEventRequest()
request.event.timestamp = int(time.time() * 1000)
request.event.message = (
    "Synchronized transporter annular confinement beam to warp frequency 0.45e17 hz"
)
request.event.notificationEnabled = True
request.event.tags["Region"] = "North"
response = agent.CreateEvent(request)
```

### Should I send events with high-frequency?

While high frequency events are supported by Formant's infrastructure, the Formant website's UX does not optimize for high frequency events in terms of searchability, navigation, and analytics. If you are thinking of sending events from one source more than once every 10 seconds, consider using a datapoint stream instead.
