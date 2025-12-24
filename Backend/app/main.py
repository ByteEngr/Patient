from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Insight Platform")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/patients", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients", response_model=list[schemas.Patient])
def read_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)