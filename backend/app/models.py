from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(String)
    city = Column(String)
    fever_temp = Column(Float)
    cough_severity = Column(Integer)
    has_covid = Column(Boolean)
