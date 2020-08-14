from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient()

    # Ingest text datapoint
    fclient.post_text("example.text", "Send text example processed")

    # Ingest numeric datapoint
    fclient.post_numeric("example.numeric", 3.0)

    # Ingest bitset datapoint
    fclient.post_bitset(
        "example.bitset", {"standing": False, "walking": False, "sitting": True}
    )

    # Ingest geolocation datapoint
    fclient.post_geolocation("example.geolocation", 22.835, 33.631667)  # lat, long

    print("Successfully ingested datapoints.")
