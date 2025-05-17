from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate

def create_user(db: Session, data: UserCreate):
    user = User(**data.dict())
    user.hash_password()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user