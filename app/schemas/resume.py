"""Module containing Pydantic schemas for resume processing and response."""
import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class ResumeResponse(BaseModel):
    """Schema for resume response data."""
    id: uuid.UUID
    filename: str
    content_type: str
    email: Optional[str] = None
    phone: Optional[str] = None
    skills: List[str] = []
    created_at: datetime

    class Config:
        from_attributes = True
