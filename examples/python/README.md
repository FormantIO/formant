## Content

This directory contains example Python scripts that interact with Formant Agent.

## Prerequisites

You can run these examples natively on your machine or through our `examples` container. You also need to have a [Formant Account](https://app.formant.io/sign-up), and a running Agent on the same local host.

We also recommend using `python3` to run all the examples.

### Docker setup

First make sure you have installed [docker](https://docs.docker.com/engine/install).

Next run:

```bash
docker run -it --net host formant/examples /bin/bash
```

This will drop you into a prompt. From there change to the `python` examples directory.

```
cd python
```

The examples container only ships with `python3` so use that when running any of the files.

### Installing Natively

You have two options to natively communicate with the agent.

#### Formant pip module

1. Make sure Formant Agent is running.
2. `pip install formant`

#### Using protos folder directly

1. Make sure Formant Agent is running.
2. `pip install -r requirements.txt`
3. Import gRPC classes from `protos` instead of from the `formant` module, e.g. `protos.agent.v1` instead of `formant.protos.agent.v1`

## Usage

Send numeric data: `python3 send_numeric.py`

Send text data via gRPC: `python3 send_text_grpc.py`

Send text data via HTTP: `python3 send_text_http.py`

Send a text file containing CSV data: `python3 send_file.py`

Send a selection intervention request via gRPC, then wait to receive the response: `python3 intervention_grpc.py`

Send a labeling intervention request via HTTP, then wait to receive the response: `python3 intervention_http.py`

Send geo-location data: `python3 send_geolocation.py`

Read application configuration: `python3 app_config.py`
