### Reading application configuration with the agent API

Before agent configuration can be queried, the Formant agent must be installed, running, and provisioned on that device.

[Installing the agent](./agent-debian-install.md)

### What is application configuration?

Application configration is a key-value (string : string) store configured on the Formant website as part of a device's configuration. Robot applications can use the agent API to read application configuration at runtime.

### How do I read application configuration?

Call `GetApplicationConfiguration` on the agent API with a `GetApplicationConfigurationRequest` object to retrieve the application configuration key-value store. Here is an example of `GetApplicationConfiguration` usage to control a simple application's rate:

```python
import grpc
import time

from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

request = agent_pb2.GetApplicationConfigurationRequest()
app_config = agent.GetApplicationConfiguration(request)
config_map = app_config.configuration.configuration_map

rate = int(config_map.get("rate_ms", "100")) / 1000
try:
    i = 1
    while True:
        print(i)
        i += i
        time.sleep(rate)
except KeyboardInterrupt:
    exit()
```

### How does a change in application configuration propagate to the device?

Any configuration change requires a restart of the formant agent. Expect agent downtime of a few seconds after saving a configuration change. When the agent comes back online and the connection is re-established, the configuration update will be reflected in calls to `GetApplicationConfiguration`.
