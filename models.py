from sqlalchemy import Column, Integer, String
from database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    education = Column(String, nullable=False)
    graduation_year = Column(Integer, nullable=False)
    experience = Column(Integer, nullable=False)
    skills = Column(String, nullable=False)
    resume_file = Column(String, nullable=False)
