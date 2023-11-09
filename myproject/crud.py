from sqlalchemy.orm import Session
from myproject.models import Festival
from myproject.models import Land
from myproject.schemas import FestivalCreate, LandCreate


def create_festival(db: Session, festival: FestivalCreate):
    db_festival = Festival(**festival.dict())
    db.add(db_festival)
    db.commit()
    db.refresh(db_festival)
    return db_festival



def delete_festival(db: Session, festival_id: int):
    festival = db.query(Festival).filter(Festival.id == festival_id).first()
    if festival:
        db.delete(festival)
        db.commit()
        return True  # Indicate that the festival was deleted
    return False  # Indicate that the festival was not found


def get_festivals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Festival).offset(skip).limit(limit).all()


def get_festival(db: Session, festival_id: int):
    return db.query(Festival).filter(Festival.id == festival_id).first()


def create_land(db: Session, land: LandCreate):
    db_land = Land(**land.dict())
    db.add(db_land)
    db.commit()
    db.refresh(db_land)
    return db_land


def get_landen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Land).offset(skip).limit(limit).all()


def get_land(db: Session, land_id: int):
    return db.query(Land).filter(Land.id == land_id).first()
