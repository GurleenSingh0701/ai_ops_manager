def recommend_playbook(risk_level):
    if risk_level == "HIGH":
        return ["Reassign owner", "Reduce scope", "Add temp capacity"]
    if risk_level == "MEDIUM":
        return ["Nudge owners", "Daily check-in"]
    return ["No action"]
