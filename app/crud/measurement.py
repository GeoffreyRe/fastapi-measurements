from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate, MeasurementUpdate
from app.crud.unit import get_unit

def create_measurement(db: Session, data: MeasurementCreate):
    unit = get_unit(db, data.unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    measurement = Measurement(**data.dict())
    db.add(measurement)
    db.commit()
    db.refresh(measurement)
    return measurement

def get_measurements(db: Session, limit=100, unit_id: int = None):
    query = db.query(Measurement)
    if unit_id is not None:
        unit = get_unit(db, unit_id)
        if not unit:
            raise HTTPException(status_code=404, detail="Unit not found")
        query = query.filter(Measurement.unit_id == unit.id)

    return query.limit(limit).all()

def get_measurement(db: Session, id: int):
    return db.query(Measurement).filter(Measurement.id == id).first()

def update_measurement(db: Session, id: int, data: MeasurementUpdate):
    data = data.dict(exclude_unset=True)
    if "unit_id" in data:
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
    measurement = get_measurement(db, id)
    if measurement:
        db.delete(measurement)
        db.commit()
    return measurement