from fastapi import FastAPI
from routes.incidents import router as incident_router
from routes.receipts import router as receipt_router
from routes.status import router as status_router

app = FastAPI(
    title="Observable Incident Agent",
    version="1.0"
)

app.include_router(incident_router)
app.include_router(receipt_router)
app.include_router(status_router)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Observable Incident Agent"
    }
