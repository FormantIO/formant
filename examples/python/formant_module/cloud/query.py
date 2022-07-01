import json
from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account

    """Example query params (only start and end time are required):
    {
        start: "2021-01-01T01:00:00.000Z",
        end: "2021-01-01T02:00:00.000Z",
        deviceIds: ["99e8ee37-0a27-4a11-bba2-521facabefa3"],
        names: ["engine_temp"],
        types: ["numeric"],
        tags: {"location":["sf","la"]},
        notNames: ["speed"],
    }
    """

    fclient = FormantClient()

    device_id = "572f5ff3-63e9-4687-b242-c0d8a4891d80"

    # query by tags
    tag_query_result = fclient.query(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "tags": {"location": ["sf"]},
        }
    )
    print(tag_query_result)

    # query by device
    device_query_result = fclient.query(
        {
            "start": "2021-01-01T00:00:00.000Z",
            "end": "2021-01-10T00:00:00.000Z",
            "deviceIds": [device_id],
        }
    )
    print(device_query_result)

    # query by filetype
    file_query_result = fclient.query(
        {
            "start": "2020-06-01T00:00:00.000Z",
            "end": "2021-06-01T00:00:00.000Z",
            "types": ["file"],
        }
    )
    print(file_query_result)

    # filter out just rosbags
    rosbags = []
    for stream in file_query_result["items"]:
        for datapoint in stream["points"]:
            device_id = stream["deviceId"]
            stream_name = stream["name"]
            file_name = datapoint[1]["filename"]
            file_size = datapoint[1]["size"]
            file_url = datapoint[1]["url"]

            if "bag" in file_name:
                rosbags.append(
                    {
                        "device_id": device_id,
                        "stream_name": stream_name,
                        "file_name": file_name,
                        "file_size": file_size,
                        "file_url": file_url,
                    }
                )

    print(rosbags)