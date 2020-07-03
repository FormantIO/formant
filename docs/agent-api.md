### Getting started with the agent API

### What is the agent API?

The Formant agent affords a gRPC- and HTTP-compatible interface, which can be used to interact with Formant on behalf of the device. We recommend using the gRPC interface, since it’s typed and more performant.

To utilize the agent API, [a Formant agent must be installed, running, and provisioned on the machine.](./agent-debian-install.md)

### What can I do with the agent API?

The following are examples of what the agent API enables:

-   Ingest telemetry datapoints
-   Trigger events
-   Update device configuration
-   Handle commands

Each of these interactions can be performed via the agent API, authenticated using the device credentials. [See the agent proto for the full set of APIs.](../protos/agent/v1/agent.proto)
