from app.models import Unit, User
from app.schemas.user import UserCreate
from app.crud.user import create_user
from sqlalchemy.orm import Session
import os

def _init_units(db: Session):
    """
    This function creates 2 units by default
    """
    for unit_name in ["Grams", "Tons"]:
        existing = db.query(Unit).filter_by(name=unit_name).first()
        if not existing:
            db.add(Unit(name=unit_name))
    db.commit()

def _init_users(db: Session):
    """
    This function creates 1 admin user
    """
    vals = {
        "username": os.getenv("ADMIN_USERNAME"),
        "email": os.getenv("ADMIN_EMAIL"),
        "password": os.getenv("ADMIN_PASSWORD")
    }

    existing = db.query(User).filter_by(email=vals["email"]).first()
    if not existing:
        create_user(db, UserCreate(**vals))

    db.commit()

def data_init(db: Session):
    _init_units(db)
    _init_users(db)