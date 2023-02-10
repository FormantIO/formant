import os
import json
import jsonschema
import datetime
from formant.sdk.agent.v1 import Client as FormantAgentClient

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

CONFIG_NAME = "config_example.json"
FILE_CREATION_TIME = 1


class JsonReader:
    def __init__(self):
        self._fclient_agent = FormantAgentClient()
        self._config_json = {}
        self._config_schema = {}
        self._observer = None
        self._json_path = None
        self._device_id = self._fclient_agent.get_agent_id()
        self._read_config()
        self._setup_watchdog()
        self._time_since_last_read = 0

    def _read_config(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        # Load config from either the agent's json blob or the config.json file
        try:
            self._config_json = json.loads(self._fclient_agent.get_config_blob_data())
            print("INFO: Loaded config from device configuration's blob data")
        except Exception as e:
            # Otherwise, load from the config.json file shipped with the adapter
            with open(f"{current_directory}/{CONFIG_NAME}") as f:
                self._config_json = json.loads(f.read())
            print("INFO: Loaded config from config.json file")

        with open(f"{current_directory}/config_schema.json") as f:
            self._config_schema = json.load(f)

        try:
            jsonschema.validate(self._config_json, self._config_schema)
            print("INFO: Validation of config json succeeded")
        except Exception as e:
            print("WARNING: Validation failed:", e)
            return

        self._set_watchdog_path()

    def _set_watchdog_path(self):
        if self._config_json != {}:
            self._json_path = self._config_json.get("json_path", None)
            print("json path is %s" % self._json_path)
        if self._json_path is None:
            print("ERROR: JSON path needs to be specified in configuration file")

    def _setup_watchdog(self):
        patterns = ["*.json"]
        ignore_patterns = None
        ignore_directories = False
        case_sensitive = True
        event_handler = PatternMatchingEventHandler(
            patterns, ignore_patterns, ignore_directories, case_sensitive
        )
        event_handler.on_created = self._config_created
        path = self._json_path
        go_recursively = False
        self._observer = Observer()
        self._observer.schedule(event_handler, path, recursive=go_recursively)
        self._observer.start()

    def close_observers(self):
        print("Killing observers")
        self._observer.stop()
        self._observer.join()

    def _config_created(self, event):
        print("INFO: %s has been created." % event.src_path)
        self._ingest_json(event.src_path)

    def _ingest_json(self, json_file):
        try:
            time.sleep(0.05)
            try:
                with open(json_file) as f:
                    json_data = json.loads(f.read())
                    if time.time() - self._time_since_last_read > FILE_CREATION_TIME:
                        print("INFO: File has been read and sent")
                        self._fclient_agent.post_json(
                            "JSON Data", json.dumps(json_data)
                        )
                        for data_field in self._config_json[
                            "json_adapter_configuration"
                        ]:
                            self._post_data(json_data, data_field)
                        self._time_since_last_read = time.time()
            except FileNotFoundError as e:
                print(e)
        except json.decoder.JSONDecodeError:
            print("File couldn't be read probably too fast")

    def _post_data(self, json_data, config_data):
        state = json_data
        tags = config_data.get("tags", {})
        index = config_data.get("indices", None)
        field = config_data.get("fields", None)

        if config_data["type"] == "numeric_set":
            data_struct = {}
            for i in range(len(config_data["paths"])):
                state_val = state
                for k in config_data["paths"][i].split("."):
                    state_val = state_val[k]
                if index is not None:
                    state_val = state_val[index[i]]
                    if field is not None:
                        state_val = state_val[field[i]]
                data_struct[config_data["data_key"][i]] = (
                    float(state_val),
                    config_data["data_units"][i],
                )
            if self._validate_data(data_struct):
                self._fclient_agent.post_numericset(
                    config_data["stream_name"], data_struct, tags=tags
                )

        elif config_data["type"] == "bool":
            data_struct = {}
            for k in config_data["paths"][0].split("."):
                state = state[k]
            if index is not None:
                state_val = state_val[index[0]]
                if field is not None:
                    state_val = state_val[field[0]]
            state_val = (state == "True") or (state == 1) or (state == "true")
            data_struct[config_data["stream_name"]] = state_val
            if self._validate_data(data_struct):
                self._fclient_agent.post_bitset(
                    config_data["stream_name"], data_struct, tags=tags
                )

        elif config_data["type"] == "bitset":
            data_struct = {}
            for i in range(len(config_data["paths"])):
                state_val = json_data
                for k in config_data["paths"][i].split("."):
                    state_val = state_val[k]
                if index is not None:
                    state_val = state_val[index[i]]
                    if field is not None:
                        state_val = state_val[field[i]]
                state_val_bitset = (
                    (state_val == "True") or (state_val == 1) or (state_val == "true")
                )
                data_struct[config_data["data_key"][i]] = state_val_bitset

            if self._validate_data(data_struct):
                self._fclient_agent.post_bitset(
                    config_data["stream_name"], data_struct, tags=tags
                )

        elif config_data["type"] == "json":
            state_val = state
            for k in config_data["paths"][0].split("."):
                state_val = state_val[k]
            if index is not None:
                state_val = state_val[index[0]]
                if field is not None:
                    state_val = state_val[field[0]]
            state_val = json.dumps(state_val)
            if self._validate_data(state_val):
                self._fclient_agent.post_json(
                    config_data["stream_name"], state_val, tags=tags
                )

        elif config_data["type"] == "numeric":
            state_val = state
            for k in config_data["paths"][0].split("."):
                state_val = state_val[k]
            if index is not None:
                state_val = state_val[index[0]]
                if field is not None:
                    state_val = state_val[field[0]]
            if self._validate_data(state_val):
                print("=====")
                print(state_val)
                self._fclient_agent.post_numeric(
                    config_data["stream_name"], float(state_val), tags=tags
                )

        elif config_data["type"] == "text":
            state_val = state
            for k in config_data["paths"][0].split("."):
                state_val = state_val[k]
            if index is not None:
                state_val = state_val[index[0]]
                if field is not None:
                    state_val = state_val[field[0]]
            if self._validate_data(state_val):
                self._fclient_agent.post_text(
                    config_data["stream_name"], str(state_val), tags=tags
                )

    def _validate_data(self, data):
        if data in ["", None, "None"]:
            return False
        else:
            return True


if __name__ == "__main__":
    try:
        reader = JsonReader()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        reader.close_observers()
