from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime

class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String, nullable=False)
    data = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
