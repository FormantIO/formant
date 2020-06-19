## Content

This directory contains example Python scripts that interact with Formant Agent.

## Setup

### Formant pip module

1. Make sure Formant Agent is running.
2. `pip install formant`

### Using protos folder directly

1. Make sure Formant Agent is running.
2. `pip install -r requirements.txt`
3. Import gRPC classes from `protos` instead of from the `formant` module, e.g. `protos.agent.v1` instead of `formant.protos.agent.v1`

## Usage

Send numeric data: `python send_numeric.py`

Send text data via gRPC: `python send_text_grpc.py`

Send text data via HTTP: `python send_text_http.py`

Send a text file containing CSV data: `python send_file.py`

Send a selection intervention request via gRPC, then wait to receive the response: `python intervention_grpc.py`

Send a labeling intervention request via HTTP, then wait to receive the response: `python intervention_http.py`

Send geo-location data: `python send_geolocation.py`

Read application configuration: `python app_config.py`
