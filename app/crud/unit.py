from sqlalchemy.orm import Session
from app.models.unit import Unit

def get_unit(db: Session, id: int):
    return db.query(Unit).filter(Unit.id == id).first()

def get_units(db: Session):
    return db.query(Unit).all()
