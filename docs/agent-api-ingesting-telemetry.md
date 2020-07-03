### Ingesting telemetry datapoints with the agent API

Before a device can ingest telemetry data, [the Formant agent must be installed, running, and provisioned on that device](./agent-debian-install.md).

### What is a telemetry datapoint?

Telemetry datapoints are individual messages posted by a Formant agent and stored in the cloud. A datapoint consists of a Formant stream name, tags (key-value pairs), timestamp, and the value itself (e.g. numeric, text, bitset).

Datapoints are also automatically tagged with the identifier of the device which posted the datapoint.

Visit the Observe documentation to see how visualization modules for your organization's telemetry datapoints are filtered, arranged, and configured.

Your organization's telemetry datapoints can be accessed programmatically via Formant's user command line tool, [fctl](./fctl.md)

### What kinds of data can I ingest with the agent API?

Any datapoint that can be streamed to Formant and visualized can be ingested via the agent API.

The Formant stream visualization types are

-   Numeric
-   Text
-   Bitset
-   Image
-   Point Cloud
-   Localization
-   JSON

[See our datapoint protobuf file for a complete reference.](../protos/model/v1/datapoint.proto)

### How do I ingest data?

First, create the datapoint(s) you wish to upload. Then, call the PostData gRPC API with the created datapoint(s).

Here is a basic example of ingesting numeric data with the agent API with python. This example assumes the `formant` python module is installed in your python environment.

```python
import grpc
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.math_pb2 import Numeric
from formant.protos.agent.v1.agent_pb2_grpc import AgentStub

channel = grpc.insecure_channel("localhost:5501")
agent = AgentStub(channel)

datapoint = Datapoint(
    stream="test.numeric", numeric=Numeric(value=3.0)
)
agent.PostData(datapoint)
```

See our examples for ingestion of more complex datapoints.

### Datapoint Throttling

If an application posts data faster than the configured throttle rate for a stream, the agent API will return `Resource Exhausted` errors. Each time this occurs, it means the datapoint was throttled and dropped.

Streams can be individually configured with different throttle rates. By default, streams are throttled at the maximum frequency of 5Hz. Configuring a stream to 0Hz will have the effect of throttling all datapoints.
