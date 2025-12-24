from pydantic import BaseModel

class PatientBase(BaseModel):
    age: int
    gender: str
    city: str
    fever_temp: float
    cough_severity: int
    has_covid: bool

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True
