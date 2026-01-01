from datetime import datetime, timedelta


def fetch_tasks():
    # placeholder: fetch from Jira API
    return [
        {"id": "OPS-1", "status": "overdue", "assignee": None,"due_at": datetime.now() + timedelta(hours=12)}
    ]

def assign_task(task_id, user):
    return f"Assigned {task_id} to {user}"
