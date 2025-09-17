from fastapi import APIRouter
from pydantic import BaseModel
from app.db.database import SessionLocal
from app.models.models import SensorData

router = APIRouter()

class SensorDataIn(BaseModel):
    sensor_type: str
    data: dict

@router.post("/ingest-data")
def ingest_data(payload: SensorDataIn):
    db = SessionLocal()
    try:
        sensor_record = SensorData(sensor_type=payload.sensor_type, data=payload.data)
        db.add(sensor_record)
        db.commit()
        return {"status": "success", "message": "Data ingested"}
    finally:
        db.close()  # ✅ Ensure session is closed


