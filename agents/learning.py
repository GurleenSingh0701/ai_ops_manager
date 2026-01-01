from memory.store import get_events

def adjust_confidence(base_confidence):
    history = get_events()
    successes = len([e for e in history if e["type"] == "AUTO_ASSIGN"])

    increment = min(successes * 0.02, 0.1)  # gradual learning
    return min(base_confidence + increment, 0.95)
