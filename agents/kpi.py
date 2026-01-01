def compute_kpis(tasks):
    total = len(tasks)
    overdue = len([t for t in tasks if t["status"] == "overdue"])
    unassigned = len([t for t in tasks if t["assignee"] is None])

    return {
        "total_tasks": total,
        "overdue_tasks": overdue,
        "unassigned_tasks": unassigned,
        "overdue_ratio": overdue / total if total else 0
    }
