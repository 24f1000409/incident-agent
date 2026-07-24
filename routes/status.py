from fastapi import APIRouter

router = APIRouter(prefix="/v2", tags=["Status"])

@router.get("/incidents/{runId}")
def status(runId: str):

    return {
        "runId": runId,
        "status": "waiting"
    }
