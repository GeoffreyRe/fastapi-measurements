from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate, MeasurementUpdate
from app.crud.unit import get_unit

def create_measurement(db: Session, data: MeasurementCreate):
    unit = get_unit(db, data.unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    m = Measurement(**data.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def get_measurements(db: Session, skip=0, limit=100):
    return db.query(Measurement).offset(skip).limit(limit).all()

def get_measurement(db: Session, id: int):
    return db.query(Measurement).filter(Measurement.id == id).first()

def update_measurement(db: Session, id: int, data: MeasurementUpdate):
    data = data.dict(exclude_unset=True)
    if data.get("unit_id"):
        unit = get_unit(db, data["unit_id"])
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
    record = db.query(Measurement).filter(Measurement.id == id).first()
    if record:
        for field, value in data.items():
            setattr(record, field, value)
        db.commit()
        db.refresh(record)

    return record

def delete_measurement(db: Session, id: int):
    m = get_measurement(db, id)
    if m:
        db.delete(m)
        db.commit()
    return m