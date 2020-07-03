### Handling commands with the agent API

Before a device can handle commands, the Formant agent must be installed, running, and provisioned on that device.

[Installing the agent](./agent-debian-install.md)

### What is a command?

A command is a message sent from user to device along a durable channel, requesting that the device perform some action.

New commands can be configured on the website to be handled on-device in application code.

There are also "built-in commands" that are selected from configurations on the website, which have pre-defined handling behavior.

### How do I handle commands?

Before a device can handle a command, the command must be configured in the Formant website.

Use `GetCommandRequestStream` on the Formant agent gRPC API to retrieve an infinite stream of all "command requests" issued to the device.

Here is a basic example of handling arbitrary commands issued to a device. All this example does is print the recevied "command request" object. This example assumes the `formant` python module is installed in your python environment.

```python
import grpc
from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

stream_request = agent_pb2.GetCommandRequestStreamRequest(command_filter=[])

for r in agent.GetCommandRequestStream(stream_request):
    print("Received command request:\n%s" % r.request)
```

This example handler will receive all commands issued to the device. The command stream will continue to be processed until the `for` loop is exited.

A filtered command request stream can be fetched by passing a "command filter" to the API call. Here is another, more in-depth example of running health checks on local sensor and motor addresses using commands. In the first example, we used the `GetCommandRequestStreamRequest` API to retrieve an infinite stream, and in this example, we will use the `GetCommandRequestRequest` and `GetCommandRequest` APIs to fetch new commands periodically.

```python
import subprocess
import time

import grpc
from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc
from formant.protos.model.v1.commands_pb2 import CommandResponse
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.text_pb2 import Text

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)


def ping(address):
    # check if the address responds within 0.1 seconds
    shell_command = ["timeout", "0.1", "ping", "-c", "1", address]
    try:
        subprocess.check_output(shell_command)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


SENSOR_ADDRESSES = ["192.168.1.28"]
MOTOR_ADDRESSES = ["192.168.30.90", "192.168.30.91", "192.168.30.92", "192.168.30.93"]

command_request_request = agent_pb2.GetCommandRequestRequest(
    command_filter=["sensor_check", "motor_check"]
)

if __name__ == "__main__":
    while True:
        command_request = agent.GetCommandRequest(command_request_request).request
        command = command_request.command
        command_request_id = command_request.id

        if command == "sensor_check":
            addresses = SENSOR_ADDRESSES
        elif command == "motor_check":
            addresses = MOTOR_ADDRESSES
        else:
            continue

        success = not (False in list(map(ping, addresses)))

        if success:
            message = "Health check succeeded"
        else:
            message = "Health check failed"

        datapoint = Datapoint(
            stream=command,
            text=Text(value=message),
            timestamp=int(time.time() * 1000.0),
        )

        command_response = CommandResponse(
            request_id=command_request_id, success=True, datapoint=datapoint
        )
        command_response = agent_pb2.SendCommandResponseRequest(
            response=command_response
        )
        agent.SendCommandResponse(command_response)

        time.sleep(0.05)

```

### Can I use request multiple command request streams with different command filters for different sets of commands?

Yes. Multiple commands streams can be handled concurrently or in separate threads.

### What if my device is offline when I issue a command?

Commands sent to offline devices are kept in the cloud until the device comes back online, at which point, commands will be transported to the device. The cloud does not deliver commands that are older than 3 days to devices.

### What if I sent a command and there are no handlers for it?

When the device receives a command and there is no active listener to immediately handle it, the command is queued on-device. The device will queue 10 commands of all types total. After 10, the oldest command is dropped when a new unhandled command is received by the device.
