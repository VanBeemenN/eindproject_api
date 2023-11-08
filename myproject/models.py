from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from myproject.database import Base


class Festival(Base):
    __tablename__ = "festivals"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    locatie = Column(String)
    start_datum = Column(Date)
    eind_datum = Column(Date)
    land_id = Column(Integer, ForeignKey("landen.id"))
    land = relationship("Land", back_populates="festivals")

class Land(Base):
    __tablename__ = "landen"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, unique=True, index=True)

    festivals = relationship("Festival", back_populates="land")
