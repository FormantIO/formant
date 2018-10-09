# Figure

This repository provides software releases and documentation for development with Figure.

## Table of Contents

-   [Quick Start](#quick-start)
-   [Agent](#agent)
    -   [Figure Agent](#figure-agent)
    -   [Figure Watcher](#figure-watcher)
    -   [Figure ROS Node](#figure-ros-node)
    -   [Datapoint Lifecycle](*datapoint-lifecycle)
    -   [Install &amp; Setup](#install--setup)
        -   [ROS Setup](#ros-setup)
    -   [Configuration](#configuration)
        -   [Figure](#figure-1)
        -   [Tags](#tags)
        -   [Streams](#streams)
        -   [Basic Stream](#basic-stream)
        -   [Tagging Streams](#tagging-streams)
        -   [Directory Stream](#directory-stream)
        -   [File Tail Stream](#file-tail-stream)
    -   [ROS Stream](#ros-stream)
    -   [Developing](#developing)
        -   [GRPC](#grpc)
        -   [HTTP](#http)

## Quick Start

1. Download the [latest release](https://github.com/FigureWorks/figure/releases) of the Figure Agent.
2. Launch the Figure Agent. Sign in with your admin credentials when asked.
3. Run one of the [examples](examples).

## Agent

The Figure Agent provides a simple managed ingestion entrypoint to the Figure Cloud.

![alt text](images/agent-architecture.png "Agent Architecture")

The Figure Agent is designed to run as a long-running daemon process. It handles communication with the Figure cloud and exposes a set of endpoints to clients on the local network. These clients, or "sources", act as a bridge between your application and Figure.

A single configuration file, `config.toml`, defines the configuration for both the Figure Agent and its sources. It should be readable by each.

### Figure Agent

The Figure Agent is the ingestion funnel to the Figure Cloud. It handles secure communication, data buffering, and in-flight compression. It exposes both a GRPC and HTTP endpoint for streaming and posting data.

### Figure Watcher

The Figure Watcher is a source capable of watching directories and tailing files.

### Figure ROS Node

The Figure ROS Node is a source capable of low-overhead forwarding of ROS topics. It provides an easy way to integrate your existing ROS stack with the Figure Agent. It will automatically subscribe to topics and stream ROS messages from those topics to the Figure Agent. The Figure Agent and Figure ROS Node communicate the message types and message descriptions necessary for the Figure Agent to parse the different message types. There is no (de)serialization overhead in the Figure ROS Node.

### Datapoint Lifecycle

The Figure Agent ingests tagged streams of datapoints. Below is a diagram describing the lifecycle of datapoints in the Figure Ecosystem.

![alt text](images/datapoint-lifecycle.png "Datapoint Lifecycle")

1. A source streams or posts a datapoint to the Figure Agent.
2. The Figure Agent does an initial validation on the datapoint to ensure it belongs to a stream defined in its configuration, has a valid timestamp (milliseconds since the epoch), and does not have empty data.
3. Upon succesful validation, the datapoint is queued for processing. For ROS datapoints we unpack the message and extract the relevant data.
4. During the processing step we apply the tags defined in the configuration.
5. After processing the datapoint is queued for upload.
6. The Figure Agent uses a small database to buffer datapoints before upload. This also allows us to store datapoints in the presence of poor network conditions, or retry failed uploads.
7. The Figure Agent batches and uploads datapoints to the Figure Cloud.
8. The Figure Dashboard will display datapoints as they arrive in the Figure Cloud.

### Install & Setup

The Figure Agent is currently available for Linux AMD 64-bit operating systems. Binaries are available in the Releases section of this repository. Debian packages, containers, and binaries for additional operating systems and architectures will be available in the near future.

The Figure Agent requires read/write access to the directory `$HOME/.figure/` where `$HOME` is the home directory of the user used to run the Figure Agent.

The Figure Cloud uses asymmetric authentication to verify the identity of each agent. To generate credentials for your agent run the Figure Agent binary. On first launch, it will prompt you to enter your admin `username` and `password`, which authenticates with the Figure Cloud and generates a unique asymmetric key for your agent. Internally, the Figure Agent periodically generates an expiring signed JWT(JSON Web Token) that the Figure Cloud uses to verify the agent's identity. These credentials are stored in `$HOME/.figure/`.

When running sources, ensure the Figure Agent is up and running first. The ROS source and the Watcher source will both attempt reconnections if the Figure Agent is not up or goes down.

If you ever delete the contents of `$HOME/.figure/`, you will need to re-run the agent provisioning step to re-generate credentials.

#### ROS Setup

The Figure Agent provides first-class support for the ingestion of ROS topics. There are several options for adding our Figure ROS Node to your ROS system.

The first, and preferred, option is to add the `figure-ros-node.par` binary to a launch file. The `par` binary contains all the necessary dependencies and manages a communication channel with the Figure Agent.

The second option is to manage the `figure-ros-node.par` binary as a binary executable, and run it after your ROS master and nodes are up. This will be a simpler path for initial development and debugging but includes the overhead of managing the lifecycle outside of a launch file.

The third option is to develop your own ROS node against the Figure Agent GRPC or HTTP endpoints. This requires manually registering ROS message descriptions with the Figure Agent.

You can find an example of a launch file in the [ROS examples](examples/ros/) directory.

### Configuration

The Figure Configuration is specified in a `toml` configuration file. This file must be located at `$HOME/.figure/config.toml` where `$HOME` is the home directory of the user used to run the Figure Agent.

Please note that both the Figure Agent and Figure sources require access to the `config.toml` file.

Here is a sample [config.toml](config.toml).

There are several important parts to this configuration.

#### Figure

```toml
[figure]
agent-server-port-grpc = "5501" #optional
agent-server-port-http = "5502" #optional
agent-server-ip = "10.10.1.10" #optional
```

The `[figure]` section configures the Figure Agent server.

`agent-server-ip`: The IP on the local network where the Figure Agent is running. (Default: `localhost`)

`agent-server-port-grpc`: The port on which the Figure Agent will  expose its GRPC endpoint. (Default: `5501`)

`agent-server-port-http`: The port on which the Figure Agent will  expose its HTTP endpoint. (Default: `5502`)

#### Tags

```toml
[tags]
site = "san_francisco_1"
environment = "dev"
group = "engineering"
```

The `[tags]` section enumerates tags used for all streaming data points. These tags will be added to every stream for this agent.

#### Streams

Streams are defined by a `toml` array. Each Stream is prefixed with a `[[streams]]` identifier. You are limited to 20 streams per agent. Streams with invalid configuration or in excess of the limit will not be accepted.

The agent will throttle high-frequency data streams to 5Hz.

#### Basic Stream

```toml
[[streams]]
name = "robot.arm.state"
```

This is the bare minimum required to identify a stream.

#### Tagging Streams

```toml
[[streams]]
name = "robot.arm.state"
[[streams.tags]]
arm="arm.12345"
```

You can also individually add tags to a stream.

#### Directory Stream

```toml
[[streams]]
name = "camera.image.drop"
dir = "/home/camera/upload"
figure-type = "image"
ext = ".jpg"
```

This is an example of a directory-watch stream used by the Figure Watcher. We need to define several properties so that the watcher knows how to parse and transmit the files to the Figure Agent.

`dir`: the directory to watch. The Figure Watcher must have read access to this directory.

`figure-type`: the Figure data type for this directory-watch stream.
We currently support the following data types for directory watching:

1. `image`
2. `video`
3. `point cloud`

`ext` : The extension to watch for. Please note the included `.` in the extension.

#### File Tail Stream

```toml
[[streams]]
name = "test.log"
filename = "/home/abraham/test.log"
file-format = "json" #optional
time-key = "timestamp" #optional
time-format = "2006-01-02T15:04:05Z07:00" #optional
```

The file-tail stream allows you to ingest a text file as datapoints (one datapoint per line).

`filename`: The absolute path to the file to tail. The Figure Watcher must have read access to this file.

`file-format`: (Optional) The format of the file. Currently the only supported format is `json`.

`time-key`: (Optional) The `key` used for timestamps in the `json` object.

`time-format`: (Optional) The format of the timestamp. The format defines how the reference time, defined to be:

`Mon Jan 2 15:04:05 -0700 MST 2006`

would be interpreted if it were the value; it serves as an example of the input format.

Here are some examples for common RFC implementations:

```toml
ANSIC       = "Mon Jan _2 15:04:05 2006"
UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
RFC822      = "02 Jan 06 15:04 MST"
RFC822Z     = "02 Jan 06 15:04 -0700" # RFC822 with numeric zone
RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" # RFC1123 with numeric zone
RFC3339     = "2006-01-02T15:04:05Z07:00"
RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
```

If the the timestamp is not provided the Figure Watcher will generate a timestamp at ingestion time.

### ROS Stream

```toml
[[streams]]
name = "abb.joint_2.position"
ros-topic = "/joint_states/joint_2"
ros-path = "data" #optional
```

ROS streams allow you to ingest ROS topics with the Figure ROS Node.

We support parsing and conversion of the following ROS data types:

1. text
2. numeric (all standard `float` and `int` message types)
3. image (from both `sensor_msgs/CompressedImage` and `sensor_msgs/Image` message types)
4. point clouds (from `sensor_msgs/PointCloud2` message type)

The optional `ros-data` parameter allows you to specify (using dot notation) a path to a subfield of the ROS message you wish to extract. If the ROS data cannot be interpreted as one of the supported ROS data types, we will attempt to translate it to `JSON` and log it as a text datapoint. Even if your message only has one value but is under a `data` key you will need to specify that in the config.

### Images as Video Stream

The Figure Cloud is capable of visualizing image telemetry as a video stream. To enable this feature, specify the `figure-type` of an image stream as `video`. For example:

```toml
[[streams]]
name = "camera.image.drop"
dir = "/home/camera/upload"
figure-type = "video"
ext = ".jpg"
```

The Figure Agent will annotate this stream as a `video` stream so it is visualized properly in the Figure Dashboard.

Similarly, you can do this with ROS streams:

```toml
[[streams]]
name = "robot.cam.001"
figure-type = "video"
ros-topic = "/image_topic"
```

### Developing

If you are using just the Figure ROS Node and the Figure Watcher to create data points then there is nothing left for you to do! However, if you want to develop against the Figure Agent and stream your own datapoints then please continue reading.

There are several ways to develop against the Figure Agent. The preferred method is via its gRPC endpoints.

#### gRPC

If you are unfamiliar with gRPC you can read about it [here](https://grpc.io/).

Once you are setup to develop against gRPC, you can take the [agent.proto](agent.proto) and generate your language-specific code stubs.

There are two ways to send data to the agent.

The `StreamData` RPC is a streaming endpoint that accepts a stream of `Data` messages.

The `PostData` RPC is a unary-type RPC that accepts single `Data` messages.

We recommend the `StreamData` endpoint for better performance.

Both `StreamData` and `PostData` accept the same `Data` message type:

```protobuf
message Data {
    // Stream name. Must match stream in config.
    string stream = 1;
    // Timestamp in miliseconds from epoch.
    int64 timestamp = 2;
    // Content Type defined by enum above.
    ContentType type = 3;
    // Raw byte data.
    bytes data = 4;
}
```

** Please note, your stream must be defined in the Figure configuration file. **

Examples of integrating with these endpoints in several languages are available in the [examples](examples/) folder.

#### HTTP

The Figure Agent also exposes a HTTP endpoint.

You can POST data to the `/v1/data` endpoint with the following JSON payload:

```json
{
    "stream": "<stream name>",
    "timestamp": 1538624058748,
    "type": "<content type>",
    "data": "<base64 encoded bytes>"
}
```

`<content type>` is `TEXT`, `NUMERIC`, `PNG`, `JPEG`, `VIDEO`, `FILE`, `POINTCLOUD`, or `ROS`.

So, for example, to send a datapoint with the text "this is a datapoint" to stream "stream.001", POST the following to `/v1/data`:

```bash
curl -v http://localhost:5502/v1/data -d '{
    "stream": "stream.001",
    "timestamp": 1538624058748,
    "type": "TEXT",
    "data": "dGhpcyBpcyBhIGRhdGFwb2ludA=="
}'
```
** For numeric types you will want to convert to a little endian byte array and encode that to base64 **

Examples of these implementations in several languages are available in [examples](examples/).
