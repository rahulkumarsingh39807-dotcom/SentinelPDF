SUSPICIOUS_KEYWORDS = [
    "/JavaScript",
    "/JS",
    "/OpenAction",
    "/Launch",
    "/AA",
    "/URI",
    "/SubmitForm",
    "/EmbeddedFile",
    "/RichMedia",
    "/ObjStm",
    "/XFA"
]


def scan_keywords(file_path):

    found = []

    with open(file_path, "rb") as pdf:

        data = pdf.read().decode(
            errors="ignore"
        )

        for keyword in SUSPICIOUS_KEYWORDS:

            if keyword in data:
                found.append(keyword)

    return found