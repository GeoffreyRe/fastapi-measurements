from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.measurement import Measurement, MeasurementCreate, MeasurementUpdate
from app.crud import measurement as crud
from app.crud.auth import get_current_user
from app.models import User
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=Measurement, status_code=201)
def create(data: MeasurementCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_measurement(db, data)

@router.get("/", response_model=list[Measurement])
def read_all(limit: int = 100, unit_id: int = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_measurements(db, limit=limit, unit_id=unit_id)

@router.get("/{id}", response_model=Measurement)
def read_one(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    measurement = crud.get_measurement(db, id)
    if not measurement:
        raise HTTPException(status_code=404, detail="Not found")
    return measurement

@router.patch("/{id}", response_model=Measurement)
def update_one(data: MeasurementUpdate, id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    measurement = crud.update_measurement(db, id, data)
    if not measurement:
        raise HTTPException(status_code=404, detail="Not found")
    return measurement

@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    measurement = crud.delete_measurement(db, id)
    if not measurement:
        raise HTTPException(status_code=404, detail="Not found")