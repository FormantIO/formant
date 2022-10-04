#!/usr/bin/env python3

import time
import json
from formant.sdk.agent.v1 import Client as FormantAgentClient
from formant.sdk.agent.adapter_utils.json_schema_validator import JsonSchemaValidator

DEFAULT_HOSTNAME = "formant.io"
DEFAULT_INTERVAL = 10
DEFAULT_TIMEOUT = 5
DEFAULT_FORMANT_STREAM = "ping"


class PingAdapter:
    """
    Formant Ping Adapter
    """

    def __init__(self):
        print("INFO: Ping Adapter has started")

        # Set up the config object
        self.config = {}
        self.config_schema = {}

        # Set up the default config params
        self.hostname = DEFAULT_HOSTNAME
        self.interval = DEFAULT_INTERVAL
        self.timeout = DEFAULT_TIMEOUT
        self.formant_stream = DEFAULT_FORMANT_STREAM

        # Set up the adapter
        self.fclient = FormantAgentClient(
            ignore_throttled=True, ignore_unavailable=True
        )
        self.json_schema_validator = JsonSchemaValidator(
            self.fclient,
            "ping_adapter_configuration",
            self.update_adapter_configuration,
        )

        # Start the ping process
        while True:
            self.ping_host()
            time.sleep(self.interval)

    def update_adapter_configuration(self, config):
        self.config = config

        # Set the config params
        self.hostname = self.config.get("hostname", DEFAULT_HOSTNAME)
        self.interval = self.config.get("interval", DEFAULT_INTERVAL)
        self.timeout = self.config.get("timeout", DEFAULT_TIMEOUT)
        self.formant_stream = self.config.get("formant_stream", DEFAULT_FORMANT_STREAM)

        # Post the startup event
        self.fclient.post_json("adapter.configuration", json.dumps(self.config))
        self.fclient.create_event(
            "Ping Adapter started",
            notify=False,
            severity="info",
        )
        print("INFO: Posted update event and config")

    def ping_host(self):
        print(self.hostname)
        print(self.interval)


if __name__ == "__main__":
    PingAdapter()
