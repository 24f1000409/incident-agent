import json

from fastapi import APIRouter, HTTPException

from services.storage import get_incident

router = APIRouter(prefix="/v2")


@router.get("/incidents/{runId}")
def status(runId):

    incident = get_incident(runId)

    if incident is None:

        raise HTTPException(
            status_code=404,
            detail="Run not found"
        )

    return json.loads(
        incident.body
    )
