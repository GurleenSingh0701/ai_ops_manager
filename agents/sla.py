from datetime import datetime, timedelta

def estimate_sla(tasks):
    now = datetime.now()
    breaches = []
    for t in tasks:
        due = t.get("due_at")
        if due:
            hours_left = (due - now).total_seconds() / 3600
            breaches.append({"task": t["id"], "hours_left": round(hours_left, 1)})
    return breaches
