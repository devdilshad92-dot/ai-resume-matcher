from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlmodel import Session
from app.core.db import engine   
from app.models.resume import Resume
from app.services.pdf import extract_text
from app.services.parser import ResumeParser
from app.schemas.resume import ResumeResponse

router = APIRouter()

@router.post("/scan", response_model=ResumeResponse)
async def scan_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # 1. Parsing Logic
    content = await file.read()
    text = extract_text(content)
    email = ResumeParser.extract_email(text)
    phone = ResumeParser.extract_phone(text)
    skills_list = ResumeParser.extract_skills(text)  
    
    # 2. Database Object 
    resume_db = Resume(
        filename=file.filename,
        content_type=file.content_type,
        extracted_text=text,
        email=email,
        phone=phone,
        skills=",".join(skills_list) if skills_list else None
    )
    
    with Session(engine) as session:
        session.add(resume_db)
        session.commit()
        session.refresh(resume_db)  
        
    return {
        "id": resume_db.id,
        "filename": resume_db.filename,
        "content_type": resume_db.content_type,
        "email": resume_db.email,
        "phone": resume_db.phone,
        "skills": skills_list,  
        "created_at": resume_db.created_at
    }