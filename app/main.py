from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import init_db
from app.api.v1.endpoints import resume

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    init_db()
    yield

app = FastAPI(title="AI Resume Matcher", lifespan=lifespan)


app.include_router(resume.router, prefix="/api/v1/resume", tags=["resume"])

@app.get("/")
def health_check():
    return {"status": "ok", "system": "active"}