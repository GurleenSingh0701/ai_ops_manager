from langgraph.graph import StateGraph

from agents.states import OpsState
from agents.decision import decide
from agents.kpi import compute_kpis
from agents.risk_signals import extract_signals
from agents.risk_forecast import forecast_risk
from agents.sla import estimate_sla
from agents.executive import executive_summary
from agents.learning import adjust_confidence

from tools.jira import fetch_tasks, assign_task
from tools.slack import notify
from memory.store import log_event, get_events


# ---------- Graph Nodes ----------

def ingest(state: OpsState):
    state["tasks"] = fetch_tasks()
    return state


def analyze(state: OpsState):
    risks = []
    for task in state["tasks"]:
        if task.get("status") == "overdue" and task.get("assignee") is None:
            risks.append({
                "task": task["id"],
                "severity": "high"
            })
    state["risks"] = risks
    return state


def kpi_node(state: OpsState):
    state["kpis"] = compute_kpis(state["tasks"])
    return state


def risk_node(state: OpsState):
    signals = extract_signals(
        state["tasks"],
        state["kpis"],
        get_events()
    )
    state["risk"] = forecast_risk(signals)
    return state


def sla_node(state: OpsState):
    state["sla"] = estimate_sla(state["tasks"])
    return state


def act(state: OpsState):
    action, base_confidence = decide(
        state["risks"],
        state["kpis"]
    )

    confidence = adjust_confidence(base_confidence)

    state["action"] = action
    state["confidence"] = confidence

    if action == "TAKE_ACTION" and state["risks"]:
        task_id = state["risks"][0]["task"]

        assign_task(task_id, "ops-user")

        log_event({
            "type": "AUTO_ASSIGN",
            "task": task_id,
            "confidence": confidence
        })

    # Always send executive summary
    notify(executive_summary(state))

    return state


# ---------- Graph Builder ----------

def build_graph():
    graph = StateGraph(OpsState)

    graph.add_node("ingest", ingest)
    graph.add_node("analyze", analyze)
    graph.add_node("kpi", kpi_node)
    graph.add_node("risk", risk_node)
    graph.add_node("sla", sla_node)
    graph.add_node("act", act)

    graph.set_entry_point("ingest")

    graph.add_edge("ingest", "analyze")
    graph.add_edge("analyze", "kpi")
    graph.add_edge("kpi", "risk")
    graph.add_edge("risk", "sla")
    graph.add_edge("sla", "act")

    return graph.compile()
