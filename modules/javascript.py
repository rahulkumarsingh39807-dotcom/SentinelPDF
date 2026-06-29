def detect_javascript(file_path):

    with open(file_path, "rb") as f:

        content = f.read().decode(
            errors="ignore"
        )

    if "/JavaScript" in content or "/JS" in content:

        return True

    return False