from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient()

    fclient.create_event(
        "Synchronized transporter annular confinement beam to warp frequency 0.4e17 hz",
        notify=True,
        tags={"Region": "North"},
    )

    print("Successfully created event.")
