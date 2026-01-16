# AI Resume Matcher

A powerful, containerized API to parse resumes (PDF) and match them against a set of skills.

## Features
- **PDF Extraction**: Efficiently extracts text from PDF documents.
- **Skill Matching**: Scans resumes for key technical skills.
- **Data Persistence**: Stores parsed data in a PostgreSQL database.
- **REST API**: Built with FastAPI for high performance and auto-generated docs.

## Setup

1. **Clone the repository**
2. **Run with Docker Compose** (Recommended):
   ```bash
   docker-compose up --build
   ```
3. **Access the API**:
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health Check: [http://localhost:8000/](http://localhost:8000/)

## Tech Stack
- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLModel/SQLAlchemy
- **PDF Parsing**: pypdf
- **Container**: Docker & Docker Compose
