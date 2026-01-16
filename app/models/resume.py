import uuid
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Resume(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    filename: str
    content_type: str
    extracted_text: str
    email: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    skills: Optional[str] = Field(default=None) 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)