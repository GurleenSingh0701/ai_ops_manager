def forecast_risk(signals):
    score = 0.0
    score += 0.5 * signals["overdue_ratio"]
    score += 0.2 if signals["unassigned"] > 0 else 0
    score += 0.2 if signals["repeat_incidents"] >= 3 else 0

    level = (
        "HIGH" if score >= 0.6 else
        "MEDIUM" if score >= 0.35 else
        "LOW"
    )
    return {"risk_score": round(score, 2), "risk_level": level}
