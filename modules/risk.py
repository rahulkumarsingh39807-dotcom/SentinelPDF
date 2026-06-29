def calculate_risk(js_found, keywords, iocs):

    score = 0

    if js_found:
        score += 30

    score += len(keywords) * 5

    score += len(iocs["urls"]) * 10

    score += len(iocs["ips"]) * 10

    if score <= 20:
        risk = "Safe"

    elif score <= 40:
        risk = "Low"

    elif score <= 70:
        risk = "Medium"

    elif score <= 90:
        risk = "High"

    else:
        risk = "Critical"

    return risk, score