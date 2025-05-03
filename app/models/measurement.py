from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    co2_value = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    unit = relationship("Unit", back_populates="measurements")
    source = Column(String)
    time = Column(DateTime, default=datetime.utcnow)
    description = Column(String, nullable=True)