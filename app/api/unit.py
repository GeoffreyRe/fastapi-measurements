from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.unit import Unit as Unit
from app.crud import unit as crud
from app.db.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Unit])
def read_all(db: Session = Depends(get_db)):
    return crud.get_units(db)

@router.get("/{id}", response_model=Unit)
def read_one(id: int, db: Session = Depends(get_db)):
    unit = crud.get_unit(db, id)
    if not unit:
        raise HTTPException(status_code=404, detail="Not found")
    return unit