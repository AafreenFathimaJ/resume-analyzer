# AI-Powered Resume Analyzer

## Overview
The AI-Powered Resume Analyzer is a web-based application designed to help students and job seekers evaluate how well their resume matches a given job description. The application provides a resume–job description match score and highlights missing keywords and skill gaps, enabling users to improve their resumes before applying.

This project is intended for academic use, placement preparation, and resume showcasing.

---

## Features
- Upload resume in PDF format  
- Input job description text  
- Resume–job description similarity score  
- Identification of missing keywords  
- Skill gap analysis presented in a readable format  
- Simple and interactive web interface  

---

## Technology Stack
- Programming Language: Python  
- Web Framework: Streamlit  
- Natural Language Processing: TF-IDF Vectorization  
- Libraries:
  - scikit-learn  
  - PyPDF2  

---

## How the Application Works
1. Text is extracted from the uploaded resume PDF  
2. The resume text and job description text are preprocessed  
3. TF-IDF vectorization is applied to both texts  
4. A similarity score is calculated  
5. Missing keywords and skill gaps are identified and displayed  

---

## Project Structure
