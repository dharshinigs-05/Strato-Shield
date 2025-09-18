from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SensorData(BaseModel):
    sensor_type: str
    data: dict

@router.post("/ingest-data")
def ingest_sensor_data(payload: SensorData):
    return {"status": "success", "received": payload}
