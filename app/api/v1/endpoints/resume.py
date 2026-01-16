from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.services.resume_service import ResumeService
from app.services.advisor import AdvisorService
from app.schemas.analysis import AnalysisResponse

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...),
    session: Session = Depends(get_session)
):
    """
    Process a resume PDF and analyze it against a job description.
    """
    # 1. Process and Save Resume
    service = ResumeService(session)
    resume = await service.process_resume(file)

    # 2. Analyze against Job Description
    advisor = AdvisorService()
    analysis_text = await advisor.analyze_resume(
        resume_text=resume.extracted_text,
        job_description=job_description
    )

    return AnalysisResponse(analysis_report=analysis_text)
