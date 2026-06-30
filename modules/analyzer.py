import json

from modules.hashes import calculate_hashes
from modules.metadata import extract_metadata
from modules.keywords import scan_keywords
from modules.javascript import detect_javascript
from modules.ioc import extract_iocs
from modules.risk import calculate_risk
from modules.parser import parse_pdf
from modules.embedded import detect_embedded


def analyze_pdf(file_path):
    hashes = calculate_hashes(file_path)
    pdf_metadata = extract_metadata(file_path)
    keywords = scan_keywords(file_path)
    javascript = detect_javascript(file_path)
    iocs = extract_iocs(file_path)
    structure = parse_pdf(file_path)
    embedded = detect_embedded(file_path)

    risk, score = calculate_risk(
        javascript,
        keywords,
        iocs
    )

    return {
        "hashes": hashes,
        "metadata": pdf_metadata,
        "keywords": keywords,
        "javascript": javascript,
        "iocs": iocs,
        "risk": risk,
        "score": score,
        "structure": structure,
        "embedded": embedded,
    }