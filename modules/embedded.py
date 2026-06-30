SUSPICIOUS = [

    "/EmbeddedFile",

    "/Launch",

    "/OpenAction",

    "/RichMedia",

    "/XFA"

]


def detect_embedded(file_path):

    with open(file_path, "rb") as pdf:

        content = pdf.read().decode(
            errors="ignore"
        )

    findings = []

    for item in SUSPICIOUS:

        if item in content:

            findings.append(item)

    return findings