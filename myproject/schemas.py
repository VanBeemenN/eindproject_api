from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class FestivalBase(BaseModel):
    naam: str
    locatie: str
    start_datum: date
    eind_datum: date


class FestivalCreate(FestivalBase):
    land_id: Optional[int] = None


class Festival(FestivalBase):
    id: int
    land_id: Optional[int] = None


    class Config:
        orm_mode = True

class LandBase(BaseModel):
    naam: str

class LandCreate(LandBase):
    pass

class Land(LandBase):
    id: Optional[int]
    festivals: List[Festival] = []

    class Config:
        orm_mode = True








