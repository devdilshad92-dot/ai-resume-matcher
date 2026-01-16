from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    job_description: str


class AnalysisResponse(BaseModel):
    analysis_report: str
