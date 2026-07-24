import json
from models.database import SessionLocal, Incident

db = SessionLocal()


def incident_exists(runId):
    return db.query(Incident).filter(
        Incident.runId == runId
    ).first()


def save_incident(data):

    obj = Incident(
        runId=data.runId,
        profile=data.profile,
        status="waiting",
        body=data.model_dump_json()
    )

    db.add(obj)
    db.commit()


def get_incident(runId):

    return db.query(
        Incident
    ).filter(
        Incident.runId == runId
    ).first()
