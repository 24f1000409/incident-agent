from fastapi import APIRouter, HTTPException

from models.schemas import IncidentRequest
from utils.validation import validate_profile
from services.storage import save_incident
from services.storage import incident_exists

router = APIRouter(prefix="/v2")


@router.post("/incidents")
def create_incident(request: IncidentRequest):

    if not validate_profile(request.profile):

        raise HTTPException(
            status_code=422,
            detail="Unsupported profile"
        )

    if incident_exists(request.runId):

        raise HTTPException(
            status_code=409,
            detail="Duplicate runId"
        )

    save_incident(request)

    return {
        "runId": request.runId,
        "status": "waiting",
        "dispatches": [],
        "approvals": []
    }
