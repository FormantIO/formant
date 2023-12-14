from formant.sdk.cloud.v2 import Client
from formant.sdk.cloud.v2.src.resources.ingest import IngestionRequest
import os
import random

if __name__ == "__main__":
    client = Client()
    ingestAPI = client.ingest

    device_id = os.environ["DEVICE_ID"]
    tags = {"location": "sf"}
    ingestion_request = IngestionRequest(device_id, tags=tags)

    # Example for numeric
    ingestion_request.add_numeric("test_numeric", random.randint(1, 100))

    # Example for text
    ingestion_request.add_text("test_text", "This is a test text.")

    # Example for json
    ingestion_request.add_json("test_json", '{"key": "value"}')

    # Example for numeric set
    numeric_set_value = [{"key1": 1.2}, {"key2": 2.3}]
    ingestion_request.add_numeric_set("test_numeric_set", numeric_set_value)

    # Example for bitset
    bitset_value = {"keys": ["bit_set_label_1", "bit_set_label_2"],  "values": [True, False]}
    ingestion_request.add_bitset("test_bitset", bitset_value)

    # Example for battery
    ingestion_request.add_battery(
        "test_battery", 85.5, voltage=3.7, current=1.5, charge=2000
    )

    # Example for health
    ingestion_request.add_health("test_health")

    # Example for location
    ingestion_request.add_location(
        "test_location", longitude=-122.4194, latitude=37.7749
    )

    # Example for image
    ingestion_request.add_image("test_image", url="https://example.com/image.jpg")

    response = ingestAPI.ingest.post(ingestion_request)
