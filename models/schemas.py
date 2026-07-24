from pydantic import BaseModel
from typing import Any

class IncidentRequest(BaseModel):
    profile: str
    runId: str
    agentName: str
    publicMarker: str
    incident: dict
    toolCatalog: list[Any]
    policy: dict
