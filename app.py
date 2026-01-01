from agents.orchestrator import build_graph

if __name__ == "__main__":
    graph = build_graph()

    initial_state = {
        "tasks": [],
        "risks": [],
        "action": "",
        "confidence": 0.0,
        "kpis": {},
        "risk": {},
        "sla": []
    }

    result = graph.invoke(initial_state)

    print("\nFINAL STATE:")
    print(result)
