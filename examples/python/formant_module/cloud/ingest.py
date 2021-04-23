from formant.sdk.cloud.v1 import Client as FormantClient

if __name__ == "__main__":
    # to authenticate set FORMANT_EMAIL and FORMANT_PASSWORD
    # environment variables for an existing service account
    # NOTE: the account must have administrator access to ingest data
    fclient = FormantClient()

    device_id = "572f5ff3-63e9-4687-b242-c0d8a4891d80"
    timestamp = 1609804800000
    tags = {"location": "sf"}

    # Ingests one of each datapoint type:
    # - numeric
    # - text
    # - json
    # - numeric set
    # - bitset
    # - battery
    # - health
    # - location
    # - point cloud
    # - file
    # - image
    # - video
    ingest_result = fclient.ingest(
        {
            "items": [
                {
                    "deviceId": device_id,
                    "name": "engine_temp",
                    "type": "numeric",
                    "tags": tags,
                    "points": [[timestamp, 100]],
                },
                {
                    "deviceId": device_id,
                    "name": "log_out",
                    "type": "text",
                    "tags": tags,
                    "points": [[timestamp, "some text"]],
                },
                {
                    "deviceId": device_id,
                    "name": "agg_status",
                    "type": "json",
                    "tags": tags,
                    "points": [[timestamp, '{"count": 20}']],
                },
                {
                    "deviceId": device_id,
                    "name": "temp",
                    "type": "numeric set",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            [
                                # unit is optional
                                {"label": "indoor", "value": 25, "unit": "C"},
                                {"label": "outdoor", "value": 10, "unit": "C"},
                            ],
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "lighting",
                    "type": "bitset",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "keys": ["tail_lights", "head_lights"],
                                "values": [True, True],
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "battery",
                    "type": "battery",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "percentage": 0.99,  # 0 to 1
                                "voltage": 1,  # Volts (optional)
                                "current": 2,  # Amps (optional)
                                "charge": 3,  # Amp-hours (optional)
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "health",
                    "type": "health",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                # status must be one of: "unknown", "operational", "offline" or "error"
                                "status": "operational",
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "location",
                    "type": "location",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "latitude": 16.917591,
                                "longitude": 149.179144,
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "laser_scan",
                    "type": "point cloud",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "url": "https://example.com/assets/scan_001.pcd",
                                "size": 1000,  # bytes
                                # optional world frame reference
                                "worldToLocal": {
                                    "translation": {
                                        "x": 0,
                                        "y": 0,
                                        "z": 0,
                                    },
                                    "rotation": {
                                        "x": 0,
                                        "y": 0,
                                        "z": 0,
                                        "w": 0,
                                    },
                                },
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "data_backup",
                    "type": "file",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "url": "https://example.com/assets/data.csv",
                                "filename": "foo.txt",
                                "size": 1000,  # bytes
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "snapshot",
                    "type": "image",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "url": "https://example.com/assets/image_001.jpg",
                                "size": 1000,  # bytes
                            },
                        ]
                    ],
                },
                {
                    "deviceId": device_id,
                    "name": "camera_feed",
                    "type": "video",
                    "tags": tags,
                    "points": [
                        [
                            timestamp,
                            {
                                "url": "https://example.com/assets/data.csv",
                                "size": 1000,  # bytes
                                "duration": 60,  # seconds
                                "mimeType": "video/mp4",  # must be mp4
                            },
                        ]
                    ],
                },
            ]
        }
    )
