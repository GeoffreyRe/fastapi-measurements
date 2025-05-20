from pydantic import BaseModel

class AuthLoginOut(BaseModel):
    access_token: str
    token_type: str = "bearer"