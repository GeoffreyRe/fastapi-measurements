from app.models.unit import Unit
from sqlalchemy.orm import Session

def _init_units(db: Session):
    for unit_name in ["Grams", "Tons"]:
        existing = db.query(Unit).filter_by(name=unit_name).first()
        if not existing:
            db.add(Unit(name=unit_name))
    db.commit()

def data_init(db: Session):
    _init_units(db)