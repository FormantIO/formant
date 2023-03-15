from formant.sdk.cloud.v2 import Client as FormantClient
from formant.sdk.cloud.v2.src.resources.queries import Query, QueryTypesItem

import dateutil.parser as parser


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
    query_api = fclient.query

    # query by tags

    start = parser.isoparse("2021-01-01T00:00:00.000Z")
    end = parser.isoparse("2021-01-10T00:00:00.000Z")
    tags = {"location": ["sf"]}
    query_model = Query(start=start, end=end, tags=tags)
    response = query_api.queries.query(query_model)
    tag_query_result = response.parsed
    print(tag_query_result)

    # query by device
    device_id = "58d7f6e1-899d-4a8a-8c02-4c805cc8227f"
    start = parser.isoparse("2021-01-01T00:00:00.000Z")
    end = parser.isoparse("2021-01-10T00:00:00.000Z")
    query_model = Query(start=start, end=end, device_ids=[device_id])
    response = query_api.queries.query(query_model)
    device_query_result = response.parsed
    print(device_query_result)

    # query by filetype

    start = parser.isoparse("2021-01-01T00:00:00.000Z")
    end = parser.isoparse("2021-01-10T00:00:00.000Z")
    types = [QueryTypesItem("file")]
    query_model = Query(start=start, end=end, types=types)
    response = query_api.queries.query(query_model)
    file_query_result = response.parsed
    # filter out just rosbags
    rosbags = []
    for stream in file_query_result.items:
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
