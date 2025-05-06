from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional
from app.schemas.unit import Unit

class MeasurementBase(BaseModel):
    co2_value: float
    source: Optional[str] = None
    description: Optional[str] = None

class MeasurementCreate(MeasurementBase):
    unit_id : int

class MeasurementUpdate(MeasurementBase):
    unit_id : Optional[int] = None

    @model_validator(mode="before")
    @classmethod
    def check_unit_id_not_null(cls, data):
        # if unit_id is given, it cannot be null
        if "unit_id" in data and data["unit_id"] is None:
            raise ValueError("unit_id cannot be null.")
        return data

class Measurement(MeasurementBase):
    id: int
    time: datetime
    unit : Unit