from datetime import date

from pydantic import BaseModel

from typing import List


class FestivalBase(BaseModel):
    naam: str
    locatie: str
    start_datum: date
    eind_datum: date

class FestivalCreate(FestivalBase):
    pass

class Festival(FestivalBase):
    id: int
    land_id: int

    class Config:
        orm_mode = True

class LandBase(BaseModel):
    naam: str

class LandCreate(LandBase):
    pass

class Land(LandBase):
    id: int
    festivals: List[Festival] = []

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

