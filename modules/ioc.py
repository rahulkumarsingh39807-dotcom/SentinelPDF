import re

URL_PATTERN = r'https?://[^\s<>"\']+'
IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'


def extract_iocs(file_path):

    with open(file_path, "rb") as f:

        content = f.read().decode(
            errors="ignore"
        )

    urls = re.findall(URL_PATTERN, content)

    ips = re.findall(IP_PATTERN, content)

    return {
        "urls": list(set(urls)),
        "ips": list(set(ips))
    }