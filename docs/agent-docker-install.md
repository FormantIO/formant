# Agent in a docker environment

The Formant agent can be setup in a docker environment in one of two ways: as part of a docker build, or as a sidcar container run alongside your application container.

## Installing into your docker build

The agent installation inside of a docker build is quite similar to a regular debian installation with a few key differences. First, we will not have an interactive GUI so we will need to turn off any user prompts. Second, we will not be provisioning the agent during the build but at runtime.

First, let's set up some `RUN` commands to get the Formant debian repo setup. (Note: you can eventually add this to a `install-formant-agent.sh` script and run as one command). It is also assumed this is run as the `root` user during the build.

```dockerfile
RUN apt-key adv --fetch-keys https://keys.formant.io/formant.pub.gpg
RUN echo "deb https://repo.formant.io/formant/debian <VERSION_CODENAME> main" | tee -a /etc/apt/sources.list > /dev/null
```

These directives setup the Formant repository. Make sure to replace `<VERSION_CODENAME>` with your linux distro.

Next set the `service_enable` debconf parameter to `false`. This ensures the normal interactive debian workflow:

```dockerfile
RUN echo formant-agent formant-agent/service_enable boolean "false" | debconf-set-selections
```

Next run the install directives for the agent:

```dockerfile
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y formant-agent --no-install-recommends
```

The last step is to startup the agent when your container starts. If you are using the entrypoint directive with a shell script you can add:

```bash
/usr/lib/formant/formant-agent &
```

You can send the agent logs to `/dev/null` as well to not intefere with your application's output:

```bash
/usr/lib/formant/formant-agent > /dev/null 2>&1 &
```

To it to run the agent as a forked process.

Many of the debconf parameters the agent takes during normal installation, are also exposed as environment variables. You can set these as you would any other docker environment variables. For ROS users, make sure to set `ROS_MASTER_URI` and `CATKIN_WS` to ensure the agent picks up the ROS runtime and your custom ROS messages.

To provision the agent, make sure that you set the `FORMANT_PROVISIONING_TOKEN` in the environment. The token is one-time use so it is safe to keen in your environment or .env file. A full example of installing the agent into a container is availble [here](../docker/debian)

## Installing the agent as a sidecar container

The Agent is available as a standalone container on [dockerhub](https://hub.docker.com/r/formant/agent)

There are a variety of tags that are avialble. Versions without a customizer are a standalone agent with no dependencies. Versions with `melodic` are based on the `ros:melodic-robot` container image. We also have `arm` and `arm64` variants of all of these.

## Running into trouble?

[See the agent installation FAQ and troubleshooting guide.](./agent-faq-and-troubleshooting.md).
