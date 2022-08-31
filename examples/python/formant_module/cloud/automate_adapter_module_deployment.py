from formant.sdk.cloud.v1 import Client as CloudClient
import uuid

DEFAULT_ADAPTER_NAME = "ros_diagnostics"
DEFAULT_EXEC_COMMAND = "./start.sh"
DEFAULT_FILE_PATH = "./adapter.zip"
DEVICE_NAME = "ESR_Turtlebot"
DEVICE_ID = "71574293-39df-48d0-826f-b75ca022eac6"
VIEW_NAME = "data-sdk"
STREAMS = ["ros_diagnostics"]
MODULE_NAME = "ROS Diagnostics"
MODULE_URL = (
    "http://localhost:3000/ros_diagnostics_configurable/?auth={auth}&device={device_id}"
)


class AutomationClient:
    def __init__(self, device_name, device_id, view_name, streams=[]):
        self._device_id = device_id
        self._device_name = device_name
        self._view_name = view_name
        self._streams = streams
        self._cloud_client = CloudClient()
        self._selected_device = self._cloud_client.query_devices(
            params={"name": self._device_name}
        )
        if len(self._selected_device["items"]) < 1:
            raise ValueError("Device not found")
        self._device_id = self._selected_device["items"][0]["id"]
        self._adapter = self._cloud_client.create_adapter(
            {
                "execCommand": DEFAULT_EXEC_COMMAND,
                "path": DEFAULT_FILE_PATH,
                "name": DEFAULT_ADAPTER_NAME,
            }
        )

    def add_adapter_to_configuration(self):
        # Query device to get configuration version
        res = self._cloud_client.get_device(self._device_id)
        _current_configuration_version = res["desiredConfigurationVersion"]

        # Query actual configuration in order to get "document" dictionary
        _config = self._cloud_client.get_device_configuration(
            self._device_id, _current_configuration_version
        )

        # Create adapter dicctinary to append to adapter list
        _current_adapter = {
            "name": self._adapter["name"],
            "execCommand": self._adapter["execCommand"],
            "fileId": self._adapter["fileId"],
            "id": self._adapter["id"],
        }
        _current_document = _config["document"]
        _current_document["adapters"].append(_current_adapter)
        body = {"document": _current_document}

        # Create new configuration and extract version number
        _new_configuration = self._cloud_client.post_device_configuration(
            self._device_id, params=body
        )
        _new_configuration_version = _new_configuration["version"]

        # Apply configuration to device
        self._cloud_client.patch_device(
            self._device_id,
            params={"desiredConfigurationVersion": _new_configuration_version},
        )

    def add_module_to_view(self, module_title, module_url):
        ##FETCH current views
        _views = self._cloud_client.get_views()

        views = []
        for view in _views["items"]:
            if view["name"] == self._view_name:
                views.append(view)

        if len(views) < 1:
            raise ValueError("View not found")

        ###GET SELECTED VIEW
        _selected_view = views[0]

        _view_layout = _selected_view["layout"]
        _new_layout = self.on_add_module(_view_layout, module_title, module_url)
        self._cloud_client.patch_view(
            view_id=views[0]["id"], params={"layout": _new_layout}
        )

    def on_add_module(self, layout, module_title, module_url):
        max_y = -1
        for module in layout:
            if layout[module]["y"] + layout[module]["height"] > max_y:
                max_y = max(max_y, layout[module]["y"] + layout[module]["height"])

        module_id = uuid.uuid4()

        layout["custom-module:%s" % module_id] = {
            "x": 0,
            "y": max_y + 1,
            "width": 8,
            "height": 6,
            "configuration": {
                "streams": self._streams,
                "customName": module_title,
                "customVisualizationUrl": module_url,
            },
        }

        return layout


client = AutomationClient(
    device_name=DEVICE_NAME,
    device_id=DEVICE_ID,
    view_name=VIEW_NAME,
    streams=STREAMS,
)

client.add_adapter_to_configuration()
client.add_module_to_view(MODULE_NAME, MODULE_URL)
