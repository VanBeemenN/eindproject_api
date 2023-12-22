

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from myproject.database import Base  # De Base-klasse die u hebt gedefinieerd

class Land(Base):
    __tablename__ = "landen"

    id = Column(Integer, primary_key=True, autoincrement=True)
    naam = Column(String, unique=True, index=True)

    festivals = relationship("Festival", back_populates="land")

class Festival(Base):
    __tablename__ = "festivals"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    locatie = Column(String)
    start_datum = Column(Date)
    eind_datum = Column(Date)
    land_id = Column(Integer, ForeignKey("landen.id"))

    land = relationship("Land", back_populates="festivals")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)  # Hier wordt het gehashte wachtwoord opgeslagen
