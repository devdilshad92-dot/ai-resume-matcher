from fastapi import UploadFile, HTTPException
from sqlmodel import Session
from app.models.resume import Resume
from app.services.pdf import extract_text
from app.services.parser import ResumeParser


class ResumeService:
    def __init__(self, session: Session):
        self.session = session

    async def process_resume(self, file: UploadFile) -> Resume:
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400, detail="Only PDF files are allowed")

        # 1. Read and Parse
        content = await file.read()
        text = extract_text(content)

        if not text:
            # Make this part robust: if text extraction fails, we might still want to save the file record
            # implies a "failed" status, but for now let's just proceed with empty text or raise
            pass

        email = ResumeParser.extract_email(text)
        phone = ResumeParser.extract_phone(text)
        skills_list = ResumeParser.extract_skills(text)

        # 2. Save to Database
        resume_db = Resume(
            filename=file.filename,
            content_type=file.content_type,
            extracted_text=text,
            email=email,
            phone=phone,
            skills=",".join(skills_list) if skills_list else None
        )

        self.session.add(resume_db)
        self.session.commit()
        self.session.refresh(resume_db)

        return resume_db
