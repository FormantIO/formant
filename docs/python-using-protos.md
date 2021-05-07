# Using the `formant` python module for Formant protobuf classes

### Installation

Installing `formant` will allow access to Formant gRPC classes in Python environments without requiring a copy of the Formant `protos` folder with your application.

`pip install formant`

This command will also install the required dependencies to communicate with the agent's gRPC interface:

```
grpcio==1.37.0
protobuf==3.7.0
six==1.12.0
grpcio-status == 1.29.0
```

The `formant` module works in Python ^2.7 and ^3.6.

### Usage

You can access the gRPC classes from the `formant` module with import statements like:

```
from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc
from formant.protos.model.v1 import commands_pb2, datapoint_pb2, file_pb2, navigation_pb2, math_pb2
```

See the [protos](https://github.com/FormantIO/formant/tree/master/formant/protos) folder in our public repo for all available protobuf types.

See [examples](https://github.com/FormantIO/formant/tree/master/examples) for how to integrate your application with Formant.
