from agents.playbook import recommend_playbook

def executive_summary(state):
    risk = state.get("risk", {"risk_level": "UNKNOWN", "risk_score": 0})
    kpis = state.get("kpis", {})
    sla = state.get("sla", [])

    playbook = recommend_playbook(risk.get("risk_level", "LOW"))

    summary = (
        f"📊 Ops Executive Summary\n"
        f"-------------------------\n"
        f"Risk Level: {risk.get('risk_level')} "
        f"(score {risk.get('risk_score')})\n"
        f"Overdue Ratio: {kpis.get('overdue_ratio', 0)}\n"
        f"Unassigned Tasks: {kpis.get('unassigned_tasks', 0)}\n"
        f"SLA Breach Window (hrs): "
        f"{[s['hours_left'] for s in sla] if sla else 'None'}\n\n"
        f"🛠 Recommended Actions:\n"
    )

    for action in playbook:
        summary += f"- {action}\n"

    return summary
