from typing import Dict, List
from datetime import datetime

EVENT_LOG: List[Dict] = []

def log_event(event: Dict):
    event["timestamp"] = datetime.now().isoformat()
    EVENT_LOG.append(event)

def get_events():
    return EVENT_LOG
