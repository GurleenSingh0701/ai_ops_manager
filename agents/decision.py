def decide(risks, kpis=None):
    if kpis and kpis.get("overdue_ratio", 0) > 0.4:
        return "TAKE_ACTION", 0.9

    if not risks:
        return "NO_ACTION", 0.95

    risk = risks[0]
    if risk["severity"] == "high":
        return "TAKE_ACTION", 0.85

    return "ESCALATE", 0.6
