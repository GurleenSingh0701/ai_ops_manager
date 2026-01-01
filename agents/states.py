from typing import TypedDict, List,Dict
class OpsState(TypedDict):
    tasks: List[dict]
    risks: List[dict]
    action: str
    confidence: float
    kpis: Dict
    risk: Dict        # ✅ ADD THIS
    sla: List[dict]   # ✅ ADD THIS
