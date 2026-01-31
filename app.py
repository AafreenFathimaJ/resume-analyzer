import streamlit as st
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI-Powered Resume Analyzer",
    layout="centered"
)

st.title("🧠 AI-Powered Resume Analyzer")
st.write(
    "Analyze your resume against a job description, calculate an ATS-style match score, "
    "and identify missing skills."
)

# ------------------ INPUTS ------------------
resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste Job Description")

# ------------------ FUNCTIONS ------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text.lower()


def clean_words(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    stopwords = {
        "and","or","the","is","in","to","of","for","with","on","within",
        "etc","etcetera","a","an","all","using","based"
    }
    return set(w for w in words if w not in stopwords and len(w) > 2)


# ------------------ ANALYSIS ------------------
if st.button("🔍 Analyze Resume"):
    if resume_file and job_description:

        resume_text = extract_text_from_pdf(resume_file)
        jd_text = job_description.lower()

        # ---- TF-IDF Similarity ----
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        similarity = (vectors * vectors.T).toarray()[0][1]

        st.success(f"📊 Resume Match Score: {round(similarity * 100, 2)}%")

        # ---- Keyword Gap ----
        resume_words = clean_words(resume_text)
        jd_words = clean_words(jd_text)
        missing_keywords = sorted(jd_words - resume_words)

        st.subheader("📌 Missing Keywords (Top 15)")
        st.write(missing_keywords[:15])

        # ---- Skill Category Analysis ----
        SKILL_CATEGORIES = {
            "Programming Languages": ["python", "java", "c", "c++"],
            "Software Development": ["testing", "debugging", "development", "coding"],
            "Methodologies": ["agile", "sdlc"],
            "Core Skills": ["problem", "solving", "collaboration", "documentation"]
        }

        st.subheader("🧠 Skill Gap Analysis")

        for category, skills in SKILL_CATEGORIES.items():
            missing = [s for s in skills if s in missing_keywords]
            if missing:
                st.write(f"❌ **{category}**: {', '.join(missing)}")
            else:
                st.write(f"✅ **{category}**: All covered")

    else:
        st.warning("⚠ Please upload a resume and paste a job description.")
