from flask import Flask, render_template, request
import fitz
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

skills_database = [
    'Python', 
    'Java', 
    'C++', 
    'JavaScript', 
    'HTML', 
    'CSS', 
    'SQL', 
    'Machine Learning', 
    'Data Analysis', 
    'Django',
    'Excel',
    'Power BI',
    'React',
    'Flask',
    'aws',
    'git'
]