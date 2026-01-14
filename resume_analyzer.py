import pdfplumber
from skills import SKILLS, JOB_ROLE_SKILLS

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def analyze_resume(file_path, role="software engineer"):
    text = extract_text(file_path)

    found_skills = [s for s in SKILLS if s in text]
    required_skills = JOB_ROLE_SKILLS[role]

    missing_skills = [s for s in required_skills if s not in found_skills]

    score = 0
    score += min(len(found_skills) * 10, 40)
    score += 30 if "education" in text else 0
    score += 30 if "project" in text else 0

    return {
        "found_skills": found_skills,
        "missing_skills": missing_skills,
        "score": score
    }
