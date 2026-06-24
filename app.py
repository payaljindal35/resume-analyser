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
