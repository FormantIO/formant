# Pre-requisites for using the formant agent python module

1. `pip install formant`, or `pip3 install formant`
2. Make sure Formant Agent is running

# Using the formant python module

This document gives a very broad overview of the capabilities of the Formant python SDK, as well as linking to examples for each capability.

## Instantiating the Formant Agent client

Each of the following requires an instantiated, connected Formant agent API client. That can be done with the following snippet:

```
from formant.sdk.agent.v1 import Client as FormantClient
fclient = FormantClient()
```

If your client find and connects to the Formant agent, a simple log will print confirming the connection:

```
INFO: Agent communication established.
```

## Ingesting data

Use the following methods of the client to ingest data into Formant:

```
post_image
post_numeric
post_numericset
post_bitset
post_text
post_geolocation
post_battery
post_json
```

Each method takes a stream name as its first argument, and the data value as its second. For instance, `fclient.post_numeric("Distance traveled", 0.23)` would post a value of `0.23` to the stream "Distance traveled".

Examples:

-   [Sending basic datapoints](./send_basic_datapoints.py)
-   [Sending images](./send_image_datapoint.py)
-   [Managing throttling](./managing_throttling.py)

## Handling commands

Use the `register_command_request_callback` and `send_command_response` methods to handle commands sent from the Formant application on your device. Refer to the examples for usage.

Examples:

-   [Handling commands](./handle_commands.py)

## Reading application configuration

Use the `get_app_config` method to retrieve application configuration values. For instance, `fclient.get_app_config("Walk mode", None)` returns the string value for the application configuration key "Walk mode" if it exists, and `None` otherwise.

Examples:

-   [Read app config](./get_app_config.py)

## Teleop

### Sending real-time data from the agent to Formant's teleop interface

#### Status Indicators

Use `post_bitset` with stream name "Status". For instance:

```
fclient.post_bitset("Status", {
    "FLIR online": False,
    "Motors responsive:" True,
    "Walk mode": False,
    "Camera mode": True,
})
```

The bitset will be streamed to the Formant teleop interface in real-time when a teleop session is active.

#### Video

Use `post_image` to stream images. If configured on the Formant app, the image stream will be encoded to a video stream by the Formant agent. Refer to [Sending images](./send_image_datapoint.py) for a basic example.

### Receiving and handling real-time data sent from Formant's teleop interface to the device

#### Buttons and joystick

Use the `register_teleop_callback` method. Example:

```
def handle_teleop_controls(datapoint):
    if datapoint.stream == "Buttons":
        handle_button(datapoint.bitset)
    elif datapoint.stream == "Joystick":
        handle_joystick(datapoint.twist)

fclient.register_teleop_callback(handle_teleop_controls)
```

Control datapoints will be streamed to the provided callback. Control datapoints with the stream name "Buttons" will contain Bitsets with the button control information. Joystick control datapoints have a user-configured stream name (although "Joystick" is a common choice) and they will contain Twists.

[Refer to our public protos](../../../protos/model/v1/math.proto) for the exact data model of Bitset and Twist.

Unregister a callback function with `unregister_teleop_callback`.

Please refer to the teleop example below for more information.

Examples:

-   [Handling and sending teleop data](./teleop.py)

### Creating events

Use the `create_event` method to create new events with levels of severity. Create an in-app notification with the `notify` keyword argument. Please refer to the example below for more information.

`create_event` method parameters:

```
message : str
notify=False : bool
tags=None : Optional[Dict[str,str]]
timestamp=None : Optional[int]
end_timestamp=None : Optional[int]
severity="info" : Literal["info", "warning", "critical", "error"]
```

Examples:

-   [Create event](./create_event.py)
