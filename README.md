# Figure

This repository provides software releases and documentation for development with Figure.

## Table of Contents

-   [Quick Start](#quick-start)
-   [Agent](#agent)
    -   [Figure Agent](#figure-agent)
    -   [Figure Watcher](#figure-watcher)
    -   [Figure ROS Bridge](#figure-ros-bridge)
    -   [Datapoint Lifecycle](#datapoint-lifecycle)
    -   [Install &amp; Setup](#install--setup)
        -   [Credentials Setup](#credentials-setup)
        -   [Debian](#debian)
        -   [Standalone Binary](#standalone-binary)
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
        -   [gRPC](#grpc)
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

### Figure ROS Bridge

The Figure ROS Bridge is a source capable of low-overhead forwarding of ROS topics. It provides an easy way to integrate your existing ROS stack with the Figure Agent. Please see [examples/ros](examples/ros) for more information.

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

The Figure Agent is currently available for Linux AMD 64-bit operating systems. Binaries and Debian packages are available in the Releases section of this repository. Debian packages are compatible with systemd. Containers and binaries for additional operating systems and architectures will be available in the near future.

When running sources, ensure the Figure Agent is up and running first. The ROS Bridge source and the Watcher source will both attempt reconnections if the Figure Agent is not up or goes down.

On startup, the Figure Agent and Watcher will check for updates and auto-update if one is available.

#### Credentials Setup

The Figure Cloud uses asymmetric authentication to verify the identity of each agent. On first launch or install, it will prompt you to enter your admin `email` and `password`, which authenticates with the Figure Cloud and generates a unique asymmetric key for your agent. Alternatively, you can set the environment variables `FIGURE_EMAIL` and `FIGURE_PASSWORD` for the initial installation and setup. This can help automate installations for larger fleets. You should also make sure to unset these environment variables after the initial installation.

Internally, the Figure Agent periodically generates an expiring signed JWT(JSON Web Token) that the Figure Cloud uses to verify the agents identity.

#### Debian

The Figure Agent debian package will setup a `figure` linux user and group. It also creates the `/home/figure` user directory where its configuration and credentials live. You should first install the Figure Agent by running:

```bash
dpkg -i figure-agent_amd64.deb
```

If you ever delete the contents of `/home/figure/`, you will be required to re-provision the Figure Agent and your `config.toml` will be erased.

To install the Figure Watcher you can run:

```bash
dpkg -i figure-watcher_amd64.deb
```

systemd makes it easy to manage the application lifecycle. By default, we do not enable auto-starting on boot the Figure Agent or Watcher. To enable this you can run:

```bash
systemctl enable figure-agent
systemctl enable figure-watcher
```

To check the status of any component:

```bash
systemctl status figure-agent
```

You can also check the log output of each using `journalctl`, for example:

```bash
journalctl -u figure-agent
```

If you make a change to the configuration file specified below you will need to run:

```bash
systemctl restart figure-agent
```

### Standalone Binary

To run the standalone Figure Agent, download the latest release and run `./figure-agent`.

The standalone Figure Agent requires read/write access to the directory `$HOME/.figure/` where `$HOME` is the home directory of the user used to run the Figure Agent components.

If you ever delete the contents of `$HOME/.figure/`, you will need to re-run the agent provisioning step to re-generate credentials.

### Configuration

The Figure Configuration is specified in a `toml` configuration file. The file location is dependent on the install type:

1. For debian packages: `/home/figure/config.toml`
2. For standalone binary: `$HOME/.figure/config.toml`

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

`agent-server-port-grpc`: The port on which the Figure Agent will expose its GRPC endpoint. (Default: `5501`)

`agent-server-port-http`: The port on which the Figure Agent will expose its HTTP endpoint. (Default: `5502`)

#### Tags

```toml
[tags]
site = "san_francisco_1"
environment = "dev"
group = "engineering"
```

The `[tags]` section enumerates tags used for all streaming data points. These tags will be added to every stream for this agent.

#### Streams

Streams are defined by a `toml` array. Each Stream is prefixed with a `[[streams]]` identifier.

Streams managed by a Figure source (such as the Figure ROS Bridge or Figure Watcher) must be defined in the configuration file.

Streams produced by a custom source will be created dynamically.

In both cases, the agent will support a maximum of 20 total streams. It automatically throttles high-frequency streams to 5Hz. It can accept datapoints up to 4MB

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
remote-agent = false #optional
```

This is an example of a directory-watch stream used by the Figure Watcher. We need to define several properties so that the watcher knows how to parse and transmit the files to the Figure Agent.

`dir`: the directory to watch. The Figure Watcher must have read access to this directory.

`figure-type`: the Figure data type for this directory-watch stream.
We currently support the following data types for directory watching:

1. `image`
2. `video`
3. `point cloud`
4. `file`

`ext` : The extension to watch for. Please note the included `.` in the extension.

`remote-agent` : If set to `false`, the Figure Watcher will stream datapoints with just the file location to the Figure Agent. If set to `true`, the Figure Watcher will read the files and send the raw file data to the Figure Agent. If set to `true` the file size limit is 2MB. This is useful to enable when your watcher and agent are running on seperate machines within a local network. (Defaults to `false`)

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

ROS streams allow you to ingest ROS topics with the Figure ROS Bridge.

We support parsing and conversion of the following ROS data types:

1. text
2. numeric (all standard `float` and `int` message types)
3. image (from both `sensor_msgs/CompressedImage` and `sensor_msgs/Image` message types)
4. point clouds (from `sensor_msgs/PointCloud2` message type)

The optional `ros-path` parameter allows you to specify (using dot notation) a path to a subfield of the ROS message you wish to extract. If the ROS data cannot be interpreted as one of the supported ROS data types, we will attempt to translate it to `JSON` and log it as a JSON datapoint. Even if your message only has one value but is under a `data` key you will need to specify that in the config.

If you would like to visualize a numeric ROS topic as text, add a `figure-type = "text"` to the stream's config:

```toml
[[streams]]
name = "abb.joint_2.position"
ros-topic = "/joint_states/joint_2"
ros-path = "data"
figure-type = "text"
```

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

### Intervention Requests

Figure supports human-in-the-loop and labeling workflows via `Intervention Requests`. Your application may use the Figure agent to issue an intervention request, then synchronously or asynchronously wait for a response from an operator.

We currently support the following types of Intervention Requests:

-   2D Bounding Box Annotation
-   Multiple Choice Selection

Please see the [Developing](#developing) section for more implementation details.

### Developing

If you are using just the Figure ROS Bridge and the Figure Watcher to create data points then there is nothing left for you to do! However, if you want to develop against the Figure Agent and stream your own datapoints then please continue reading.

There are several ways to develop against the Figure Agent. The preferred method is via its gRPC endpoints.

#### gRPC

If you are unfamiliar with gRPC you can read about it [here](https://grpc.io/).

Once you are setup to develop against gRPC, you can take the [agent.proto](agent.proto) and generate your language-specific code stubs.

There are two ways to send data to the agent.

The `StreamData` RPC is a streaming endpoint that accepts a stream of `Data` messages.

The `PostData` RPC is a unary-type RPC that accepts single `Data` messages.

We recommend the `StreamData` endpoint for better performance.

Both `StreamData` and `PostData` accept the same `Datapoint` message type defined in [agent.proto](agent.proto).

For Intervention Requests there are several important rpc's:

The `CreateInterventionRequest` rpc will create a InterventionRequest. It will return a `InterventionRequest` object that contains the `id`. You will use this `id` to retrieve responses.

The `GetInterventionRequest` rpc will get the `InterventionRequest` specified by the `id` in the request object. It will return a `InterventionRequest`. You can use this rpc to poll for responses.

The `GetInterventionResponse` rpc accepts a `request_id` and will block until a response has been generated by a user. We recommend this rpc for taking actions based on user input to a `InterventionRequest`. You should use this rpc to avoid implementing any polling logic on the `GetInterventionRequest` rpc.

Examples of integrating with these endpoints in several languages are available in the [examples](examples/) folder.

#### HTTP

The Figure Agent also exposes a HTTP endpoint.

You can `POST` data to the `/v1/data` endpoint with the following JSON payload:

```json
{
    "stream": "<stream name>",
    "timestamp": 1538624058748,
    "<data_type>": { <data_object> }
}
```

So, for example, to send a datapoint with the text "this is a datapoint" to stream "stream.001", POST the following to `/v1/data`:

```bash
curl -v http://localhost:5502/v1/data -d '{
    "stream": "stream.001",
    "timestamp": 1538624058748,
    "text" : {"value" : "this is a datapoint" }
}'
```

** For `bytes` types you will need to encode as a base64 string**

You can create Intervention Requests with a `POST` to the `/v1/intervention-requests` endpoint. Here is an example is of a `selection` Intervention Request:

```json
{
    "timestamp": 1538624058748,
    "severity": "INFO",
    "selection_request": {
        "image": {
            "content_type": "image/png",
            "url": "file://path/to/image"
        },
        "hint": 0,
        "options": ["option 1", "option 2", "option 3"],
        "instruction": "Please select one of these options",
        "tags": {
            "tag1": "tagvalue1"
        }
    }
}
```

To check on the status of a Intervention Request, use a `GET` on `/v1/intervention-requests/:id` where `:id` is the `id` returned when creating an Intervention Request.

To wait for an Intervention Response, use a `GET` on `/v1/intervention-responses/:id` where `:id` is the `id` returned when creating an Intervention Request. This will block till a response is generated.

Examples of these implementations in several languages are available in [examples](examples/).
