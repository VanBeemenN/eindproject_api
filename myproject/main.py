import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi.responses import FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine

if not os.path.exists('./sqlitedb'):
    os.mkdir('./sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBasic()

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"vanbe": credentials.username, "ITF": credentials.password}


## Nieuwe endpoints voor festivals
## POST NAAR /festivals
@app.post("/festivals", response_model=schemas.Festival)
def create_festival(festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    return crud.create_festival(db, festival=festival)


## GET /festivals/?skip=&limit=
@app.get("/festivals", response_model=list[schemas.Festival])
async def read_festivals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    festivals = crud.get_festivals(db, skip=skip, limit=limit)
    return festivals


## GET /festivals/{festival_id}
@app.get("/festivals/{festival_id}", response_model=schemas.Festival)
def read_festival(festival_id: int, db: Session = Depends(get_db)):
    festival = crud.get_festival(db, festival_id=festival_id)
    if festival is None:
        raise HTTPException(status_code=404, detail="Festival not found")
    return festival


@app.delete("/festivals/{festival_id}", response_model=bool)
def delete_festival(festival_id: int, db: Session = Depends(get_db)):
    result = crud.delete_festival(db, festival_id)
    if result:
        return True  # Festival was deleted
    raise HTTPException(status_code=404, detail="Festival not found")


## Nieuwe endpoints voor landen
## POST NAAR /landen
@app.post("/landen", response_model=schemas.Land)
def create_land(land: schemas.LandCreate, db: Session = Depends(get_db)):
    return crud.create_land(db, land=land)


## GET /landen/?skip=&limit=
@app.get("/landen", response_model=list[schemas.Land])
def read_landen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    landen = crud.get_landen(db, skip=skip, limit=limit)
    return landen


## GET /landen/{land_id}
@app.get("/landen/{land_id}", response_model=schemas.Land)
def read_land(land_id: int, db: Session = Depends(get_db)):
    land = crud.get_land(db, land_id=land_id)
    if land is None:
        raise HTTPException(status_code=404, detail="Land not found")
    return land


@app.get("/")
def get_index():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(index_path)


@app.post("/create_festival")
async def create_festival(festival_data: schemas.FestivalCreate, db: Session = Depends(get_db)):
    # Your code to handle the festival creation
    # You can access the festival data using the festival_data variable
    created_festival = crud.create_festival(db, festival_data=festival_data)

    # For example, you might print the data for testing purposes
    print("Received Festival Data:")
    print(festival_data.dict())

    # Return a response or raise an exception based on success or failure
    return {"message": "Festival created successfully"}


# Functie om de database-sessie op te halen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
