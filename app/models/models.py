from sqlalchemy import Column, Integer, String, JSON
from app.db.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String, index=True)
    data = Column(JSON)

