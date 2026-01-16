import os
import logging
from openai import AsyncOpenAI
from app.core.prompts import ATS_ANALYSIS_PROMPT

logger = logging.getLogger(__name__)


class AdvisorService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = None
        if self.api_key:
            self.client = AsyncOpenAI(api_key=self.api_key)
        else:
            logger.warning(
                "OPENAI_API_KEY is not set. AI features will not work.")

    async def analyze_resume(self, resume_text: str, job_description: str) -> str:
        if not self.client:
            return "Error: OpenAI API Key is missing. Please set OPENAI_API_KEY in your environment."

        prompt = ATS_ANALYSIS_PROMPT.format(
            resume_text=resume_text,
            job_description=job_description
        )

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o",  # Using a high-quality model for complex analysis
                messages=[
                    {"role": "system",
                        "content": "You are a helpful expert ATS consultant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {e}")
            return f"Error creating analysis: {str(e)}"
