import datetime
from formant.sdk.cloud.v1 import Client as FormantClient
from formant.sdk.cloud.v1.types import Annotation, AnnotationTemplateListResult
import random

DEVICE_ID = "b0990d5a-cdff-4c3c-ab71-c6c72be385ad"
ANNOTATION_TEMPLATE_NAME = "Mission"


def main():
    fclient = FormantClient()
    print("Finding Templates...")
    annotation_templates = AnnotationTemplateListResult(
        fclient.get_annotation_templates()
    )
    bug_report_template = annotation_templates.get_by_name(ANNOTATION_TEMPLATE_NAME)
    if bug_report_template is None:
        print(
            "No annotation template named '%s', please configure Annotation Templates in the Formant UI."
            % ANNOTATION_TEMPLATE_NAME
        )
        return
    print("Setting up Annotation...")
    annotation = Annotation.from_template(
        bug_report_template,
        DEVICE_ID,
        "Mission Completed",
    )
    # Set predefined fields
    for field in bug_report_template.get_required_tag_fields():
        annotation.set_tag(field.key, random.choice(field.tag_choices))
    start_time = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
        minutes=1
    )
    annotation.set_start_time(start_time)
    annotation.set_duration(1)
    print("Posting Annotation...")
    fclient.post_annotation(annotation.get_request_params())
    print("Annotation created.")

    # Annotations don't need to be linked with a template
    annotation = Annotation(DEVICE_ID, "Mission Success", "Mission Completed")

    # Tags can be set arbitrarially
    annotation.set_tag("Status", "Succesful")
    annotation.set_tag("Mission Type", "Short")
    annotation.set_tag("Route", "1")
    start_time = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
        minutes=1
    )
    annotation.set_start_time(start_time)
    annotation.set_duration(1)
    print("Posting Annotation...")
    fclient.post_annotation(annotation.get_request_params())
    print("Annotation created.")


if __name__ == "__main__":
    main()
