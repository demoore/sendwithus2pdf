import os

import pdfkit
import sendwithus

from slugify import slugify

API_KEY = os.getenv("SWU_API_KEY")
client = sendwithus.api(api_key=API_KEY)

FAILURES = []


def capture_failure(template_json, version_json, exception):
    line = "\t".join(
        map(
            str,
            [
                template_json["id"],
                template_json["locale"],
                version_json["id"],
                exception,
            ],
        )
    )
    FAILURES.append(line)


def run():
    for template in client.templates().json():
        for version in template["versions"]:
            try:
                v = client.get_template(template["id"], version=version["id"]).json()
            except Exception as e:
                print(
                    f"Failed to get {version['id']} for {template['name']} - {template['id']} - {template['locale']}\n{e}"
                )

                continue

            file_name = f"{template['name'][:20]}-{template['locale']}-{v['name'][:20]}-{template['id']}-{v['id']}"

            try:
                rendered = client.render(
                    email_id=template["id"], email_data={}, version_name=v["name"]
                ).json()
            except Exception as e:
                print(
                    f"Failed to render {version['id']} for {template['name']} - {template['id']} - {template['locale']}\n{e}"
                )
                continue

            try:
                pdfkit.from_string(
                    rendered["html"],
                    "out/" + slugify(file_name, separator="_") + ".pdf",
                )
                print(f"Generated PDF for... {template['id']} - {v['id']}")
            except Exception as e:
                print(
                    f"Failed to create PDF for {version['id']} for {template['name']} - {template['id']} - {template['locale']}\n{e}"
                )
                continue

    print(f"Got {len(FAILURES)} failures")
    for f in FAILURES:
        print(f)


# Capture failures to show at the end
if __name__ == "__main__":
    run()
else:
    run()
