from pydantic import BaseModel

class UnitBase(BaseModel):
    name: str

class Unit(UnitBase):
    id: int