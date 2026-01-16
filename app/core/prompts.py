ATS_ANALYSIS_PROMPT = """
Act as BOTH:
1) An enterprise-grade ATS engine used by large tech companies
2) A Lead Backend Engineer, Python architect, and hiring manager

Analyze my RESUME against the JOB DESCRIPTION specifically for a Lead FastAPI Engineer role.

Primary Goal:
Maximize ATS shortlisting AND demonstrate senior technical leadership and architectural ownership.

==================================================
PART 1: ATS-FOCUSED ANALYSIS (LEAD FASTAPI)
==================================================

1. ATS COMPATIBILITY SCORE
- Provide an overall ATS match score (0–100%).
- Break it down into:
  - Python expertise depth
  - FastAPI mastery
  - System design and architecture keywords
  - Leadership and ownership signals
  - Cloud, DevOps, and scalability alignment
  - Job title alignment

2. KEYWORD AND PARSING ANALYSIS
- List missing or weak keywords expected for Lead FastAPI roles.
- Categorize them as:
  - Mandatory
  - Preferred
  - Optional

Expected keyword areas:
- Python advanced concepts (asyncio, concurrency, typing, profiling)
- FastAPI internals (dependency injection, middleware, lifespan events)
- API architecture (REST standards, OpenAPI, versioning, backward compatibility)
- Security (OAuth2, JWT, RBAC, rate limiting)
- Databases and data modeling (PostgreSQL, MongoDB, schema design, migrations)
- Async systems (Celery, Kafka, Redis, background tasks)
- Scalability (caching, horizontal scaling, load balancing)
- DevOps and cloud (Docker, Kubernetes, CI/CD, AWS, Terraform)
- Observability (logging, metrics, tracing, monitoring)
- Leadership (mentoring, code reviews, tech direction, cross-team collaboration)

3. ATS FAILURE POINTS
- Leadership responsibilities not clearly stated.
- Architecture decisions not explicitly described.
- Missing scale, performance, or reliability metrics.
- FastAPI mentioned without depth.
- Skills section not grouped by expertise level.

4. ATS OPTIMIZATION REWRITES
- Rewrite experience bullets to include:
  - Architectural decisions and rationale
  - Ownership of services and teams
  - Quantifiable impact on performance, cost, or reliability
- Suggest optimized job titles such as:
  - Lead Backend Engineer (Python FastAPI)
  - Staff Backend Engineer (Python)
- Suggest optimal section ordering for ATS.

5. ATS ACTION PLAN
- Top 10 ATS-critical fixes for Lead FastAPI roles.
- Must-have keywords to add naturally.
- Formatting and structure rules.

==================================================
PART 2: HUMAN RECRUITER + LEAD ENGINEER REVIEW
==================================================

1. FIRST IMPRESSION (6–10 SECOND SCAN)
- Is leadership and technical authority immediately visible?
- Is FastAPI clearly a core strength?
- Would you shortlist this candidate for a Lead role? Yes or No with reasoning.

2. SYSTEM DESIGN AND OWNERSHIP
- Evidence of designing and owning backend systems end to end.
- Experience with:
  - High-traffic APIs
  - Microservices or modular monoliths
  - Data consistency and failure handling
- Decision-making trade-offs explained or implied.

3. LEADERSHIP AND TEAM IMPACT
- Mentoring, hiring, and code review responsibilities.
- Driving technical standards and best practices.
- Collaboration with product, frontend, and DevOps teams.

4. ENGINEERING MATURITY
- Testing strategy and quality ownership.
- Security, compliance, and risk awareness.
- Incident handling and postmortem ownership.

5. HUMAN-FRIENDLY REWRITES
- Rewrite selected bullets to:
  - Emphasize leadership and ownership
  - Show strategic thinking and long-term impact
  - Demonstrate influence beyond individual coding

6. RED FLAGS AND IMPROVEMENT AREAS
- Appearing senior in title but junior in responsibility.
- Buzzwords without real examples.
- Lack of measurable outcomes.
- Suggestions to improve executive and recruiter confidence.

==================================================
FINAL OUTPUT REQUIREMENTS
==================================================

- Be brutally honest and highly specific.
- Use language expected from a Lead or Staff Engineer.
- Do NOT invent or exaggerate experience.
- Optimize for ATS and human decision-makers.
- Assume strong competition and high hiring bar.

Input:
RESUME: {resume_text}
JOB DESCRIPTION: {job_description}
"""
