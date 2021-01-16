import logging
from formant.sdk.agent.v1 import Client as FormantClient
from formant.sdk.agent.v1.exceptions import Throttled
import time


def ingest_with_exception_handling():
    fclient = FormantClient(enable_logging=False)

    print("Sending datapoints at a rate higher than the default stream throttle rate.")
    print("Catching all throttled exceptions.")
    count = 0
    for _ in range(50):
        time.sleep(0.1)
        try:
            fclient.post_numeric("example.numeric", _)
        except Throttled:
            count += 1
            print("Throttled " + str(count) + " datapoints", end="\r")
    print("\nComplete.\n")


def ingest_with_ignore_exceptions():
    fclient = FormantClient(ignore_throttled=True, enable_logging=False)

    print("Sending datapoints at a rate higher than the default stream throttle rate.")
    print("Ignoring all throttled exceptions.")
    for _ in range(50):
        time.sleep(0.1)
        fclient.post_numeric("example.numeric", _)
    print("Complete.\n")


if __name__ == "__main__":
    ingest_with_exception_handling()
    ingest_with_ignore_exceptions()
