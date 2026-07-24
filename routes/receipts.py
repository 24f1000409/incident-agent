from fastapi import APIRouter

router = APIRouter(prefix="/v2", tags=["Receipts"])

@router.post("/incidents/{runId}/receipts")
def receipt(runId: str):

    return {
        "runId": runId,
        "status": "receipt accepted"
    }
