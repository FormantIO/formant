## Content

This directory contains usage examples for the Formant Agent with Docker.

## Setup

1. Make sure you have [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Usage

1. Go to the [Create Agent](https://app.formant.io/create-agent) page and enter a agent name and tags.
2. On the Installer page, copy and paste your `FORMANT_PROVISIONING_TOKEN` from the install step into the [formant.env](formant.env) file.
3. Run `docker-compose up` to start the Formant Agent container.

## Notes

### Image Repository

The full list of available images can be found on [Docker Hub](https://hub.docker.com/r/formant/agent/tags).

Our container images have support for AMD64, ARM64, and ARM. We provide both ROS Melodic and ROS Kinetic variants as well.

### ROS

We have included a ROS-based [docker-compose](ros/docker-compose.yaml) as well. This will start up two containers, one running a ROS Master and our Agent. You should note the [formant.env](ros/formant.env) file contains the `ROS_MASTER_URI` pointed to the container over the `formant` docker network.

### Container State

The agent uses a docker volume to store state and persistent data. If the volume is deleted you will need to reprovision the agent.

The provisioning token you use to initialize the agent is a one-time use token. You can remove it from the [formant.env](formant.env) file after the credentialing process is done.

### MacOS

Docker for Mac users may need to set `FORMANT_AGENT_IP=0.0.0.0` in the [formant.env](formant.env) file in order to access the local HTTP/GRPC interface from their host machine.
This is to ensure that the Formant agent is reachable from outside its container networking namespace.
