import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import init_db
from app.api.v1.endpoints import resume

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Creating tables...")
    init_db()
    yield

app = FastAPI(title="AI Resume Matcher", lifespan=lifespan)


app.include_router(resume.router, prefix="/api/v1/resume", tags=["resume"])


@app.get("/")
def health_check():
    return {"status": "ok", "system": "active"}
