from flask import Flask, render_template, request
import fitz
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

skills_database = [
    "python", 
    "java", 
    "c++", 
    "javascript", 
    "html", 
    "css", 
    "sql", 
    "machine learning", 
    "data analysis", 
    "django",
    "excel",
    "power bi",
    "react",
    "flask",
    "aws",
    "git"
]

def extract_text(pdf_path):
    text = ""
    
    pdf = fitz.open(pdf_path)

    for page in pdf:
        text += page.get_text()
    return text.lower()

def analyze_resume(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    found_skills = []
    missing_skills = []

    for skill in skills_database:
        if skill in resume_text:
            found_skills.append(skill)
        if skill in job_description and skill not in resume_text:
            missing_skills.append(skill)
    
    total_required = len(found_skills) + len(missing_skills)

    if total_required == 0:
        score = 0
    else:
        score = int((len(found_skills) / total_required) * 100)

    return score, found_skills, missing_skills