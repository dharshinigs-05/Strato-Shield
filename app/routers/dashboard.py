from fastapi import APIRouter

router = APIRouter()

@router.get("/risk-index")
def get_risk_index():
    return {"risk_index": 0.72, "status": "High"}

@router.get("/alerts")
def get_alerts():
    return [
        {"id": 1, "type": "Rockfall Risk", "level": "High", "time": "2025-09-18 10:30"},
        {"id": 2, "type": "Weather", "level": "Moderate", "time": "2025-09-18 09:15"},
    ]

@router.get("/events")
def get_events():
    return [
        {"id": 101, "description": "Rockfall detected near Zone A", "date": "2025-09-10"},
        {"id": 102, "description": "Heavy rainfall warning", "date": "2025-09-12"},
    ]

@router.get("/workers")
def get_workers():
    return [
        {"id": 1, "name": "Raj", "location": "Zone A"},
        {"id": 2, "name": "Meena", "location": "Zone B"},
    ]
