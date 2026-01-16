import os
from sqlmodel import SQLModel, create_engine
from app.models.resume import Resume

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://dilshad:password@db:5432/resumedb")

engine = create_engine(DATABASE_URL)


def init_db():
    SQLModel.metadata.create_all(engine)
