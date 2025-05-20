from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.schemas.auth import AuthLoginOut
from app.models import User
from app.crud import auth as crud
from app.crud.auth import get_current_user
from app.models import User
from app.db.database import get_db
from typing import Annotated

router = APIRouter()

@router.post("/login", response_model=AuthLoginOut)
def login(username: Annotated[str, Form()], password: Annotated[str, Form()], db: Session = Depends(get_db)):
    try:
        return crud.generate_jwt(username=username, password=password, db=db)
    except KeyError:
        raise HTTPException(status_code=403, detail="Authentication failed.")