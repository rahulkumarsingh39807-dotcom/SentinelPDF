import re


def parse_pdf(file_path):

    with open(file_path, "rb") as pdf:

        content = pdf.read().decode(
            errors="ignore"
        )

    result = {

        "objects": len(
            re.findall(r"\d+\s+\d+\s+obj", content)
        ),

        "streams": content.count("stream"),

        "endstreams": content.count("endstream"),

        "xref": content.count("xref"),

        "trailer": content.count("trailer"),

        "pages": content.count("/Page"),

        "objstm": "/ObjStm" in content,

        "xref_stream": "/XRef" in content

    }

    return result