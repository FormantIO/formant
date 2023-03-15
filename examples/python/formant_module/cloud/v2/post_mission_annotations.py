from datetime import datetime, timezone, timedelta

from formant.sdk.cloud.v2 import Client as FormantClient

from formant.sdk.cloud.v2.src.resources.annotations import AnnotationTags, Annotation


from typing import Dict
import random

DEVICE_ID = "b0990d5a-cdff-4c3c-ab71-c6c72be385ad"
ANNOTATION_TEMPLATE_NAME = "Mission"


def main():
    fclient = FormantClient()
    admin_api = fclient.admin

    # Annotations don't need to be linked with a template

    annotation_tags = AnnotationTags()
    annotation_tags.additional_properties = {
        "Status": "Succesful",
        "Mission Type": "Short",
        "Route": "1",
    }

    annotation = Annotation(
        user_id=DEVICE_ID,
        time=datetime.now(),
        note="Mission Completed",
        tags=annotation_tags,
    )
    # Tags can be set arbitrarially

    start_time = datetime.now(tz=timezone.utc) - timedelta(minutes=1)

    end_time = start_time + timedelta(minutes=1)
    annotation.time = start_time
    annotation.end_time = end_time
    print("Posting Annotation...")
    _ = admin_api.annotations.post(annotation)
    print("Annotation created.")


if __name__ == "__main__":
    main()
