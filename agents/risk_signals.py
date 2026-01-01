def extract_signals(tasks, kpis, history):
    signals = {
        "overdue_ratio": kpis.get("overdue_ratio", 0),
        "unassigned": sum(1 for t in tasks if t.get("assignee") is None),
        "repeat_incidents": sum(1 for e in history if e["type"] == "AUTO_ASSIGN"),
        "velocity_drop": kpis.get("velocity_drop", 0),  # stub for now
    }
    return signals
