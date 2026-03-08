from fastapi import HTTPException
from fastapi import FastAPI, UploadFile, File, Form
import models
from database import engine, SessionLocal
import os
import shutil

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Health Check Endpoint
@app.get("/health")
def health():
    return {"status": "API is running"}


# Create Candidate and Upload Resume
@app.post("/candidates")
async def create_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    experience: int = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...)
):

    db = SessionLocal()

    # Create resumes folder if it doesn't exist
    os.makedirs("resumes", exist_ok=True)

    file_path = f"resumes/{resume.filename}"

    # Save resume file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # Store candidate in database
    new_candidate = models.Candidate(
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        address=address,
        education=education,
        graduation_year=graduation_year,
        experience=experience,
        skills=skills,
        resume_file=file_path
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    db.close()

    return {
        "message": "Candidate stored in database",
        "candidate_id": new_candidate.id
    }


# Get All Candidates
@app.get("/candidates")
def get_all_candidates():

    db = SessionLocal()

    candidates = db.query(models.Candidate).all()

    db.close()

    return {
        "count": len(candidates),
        "data": candidates
    }


# Get Candidate by ID
@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):

    db = SessionLocal()

    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()

    db.close()

    if not candidate:
        return {"error": "Candidate not found"}

    return candidate


# Delete Candidate
@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):

    db = SessionLocal()

    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()

    if not candidate:
        db.close()
        return {"error": "Candidate not found"}

    db.delete(candidate)
    db.commit()
    db.close()

    return {"message": "Candidate deleted successfully"}

