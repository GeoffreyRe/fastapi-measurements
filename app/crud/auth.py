from sqlalchemy.orm import Session
from app.schemas.auth import AuthLoginOut
from app.models import User
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.db.database import get_db
import jwt
import datetime
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def generate_jwt(username: str, password: str, db: Session):
    user = db.query(User).filter(User.email == username).first()
    if not user:
        raise KeyError()

    pwd_id_correct = user.check_password(password)

    if not pwd_id_correct:
        raise KeyError()

    claims = {
        "username": user.username,
        "sub": str(user.id),
        "iat": datetime.datetime.now(),
    }
    token = jwt.encode(claims, os.getenv('SECRET_KEY'), algorithm="HS256")
    return AuthLoginOut(access_token=token)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        data = jwt.decode(token, os.getenv('SECRET_KEY'), ['HS256'])
        user = db.query(User).filter(User.id ==int(data.get("sub"))).first()
    except Exception as e:
        raise HTTPException(status_code=403, detail="Token invalid.")
    
    return user

