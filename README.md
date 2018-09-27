# Figure

This repository provides releases and documentation on how to develop with the Figure SDK, Agent, and other Figure tools.

## Agent

The Figure Agent provides a simple and reliable ingestion entrypoint for the Figure Cloud.

#### Figure Agent Server

The Figure Agent Server is the ingestion funnel to the Figure Cloud. It handles secure communication, data buffering and compression, as well as exposing both a GRPC and HTTP endpoint for streaming data.


#### Figure Agent Watcher

The Figure Agent Watcher manages watching directories and tailing files. It automatically will connect to the Figure Agent Server and stream data specified in the configuration to it.


#### Figure Agent ROS Node

The Figure Agent ROS Node provides a easy way tointegrate your existing ROS stack with the Figure Agent. It will automatically listen to topics specified in the configuration and stream data from those topics to the Figure Agent Server.

### Install & Setup

Currently the Figure Agent can be installed natively on Linux 64 bit OS's. Additionally, there are containers available for all components.


### Configuration

