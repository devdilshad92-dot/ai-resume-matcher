import re
from app.core.config import SKILL_SET

class ResumeParser:
    
    @staticmethod
    def extract_email(text: str):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        match = re.search(email_pattern, text)
        return match.group(0) if match else None

    @staticmethod
    def extract_phone(text: str):
        phone_pattern = r'\b\d{10,12}\b'
        match = re.search(phone_pattern, text)
        return match.group(0) if match else None

    @staticmethod
    def extract_skills(text: str):
        text_lower = text.lower()
        found_skills = []
        
        for skill in SKILL_SET:
            if skill.lower() in text_lower:
                found_skills.append(skill)
        
        return found_skills