from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SensorData(BaseModel):
    sensor_type: str
    data: dict

# Core API: Ingest sensor data
@router.post("/ingest-data")
def ingest_sensor_data(payload: SensorData):
    return {"status": "success", "received": payload}

# Test API: Simple GET to verify router works
@router.get("/test")
def test_sensor():
    return {"message": "Sensor API is working"}


