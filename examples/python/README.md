## Content

This directory contains example Python scripts that interact with Formant Agent.

## Setup

1. Make sure Formant Agent is running.
2. `pip install -r requirements.txt`

## Usage

Send numeric data: `python send_numeric.py`

Send text data via GRPC: `python send_text_grpc.py`

Send text data via HTTP: `python send_text_http.py`

Send a text file containing CSV data: `python send_file.py`

Send a selection intervention request via GRPC, then wait to receive the response: `python intervention_grpc.py`

Send a labeling intervention request via HTTP, then wait to receive the response: `python intervention_http.py`

Send geo-location data: `python send_geolocation.py`
