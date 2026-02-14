import streamlit as st
import requests
import PyPDF2

API_URL = "http://127.0.0.1:8000/analyze"

st.title("🚀 Career Navigator AI")

mode = st.radio(
    "Choose Input Method",
    ["Type Skills & Interests", "Upload Resume (PDF)"]
)

name = st.text_input("Your Name")
education = st.text_input("Education")

skills = ""
interests = ""

COMMON_SKILLS = [
    "python", "django", "machine learning",
    "sql", "pandas", "numpy",
    "tensorflow", "react", "flask"
]

def extract_skills(text):
    text = text.lower()
    return ", ".join(
        [skill for skill in COMMON_SKILLS if skill in text]
    )

if mode == "Type Skills & Interests":
    skills = st.text_input("Skills (comma separated)")
    interests = st.text_input("Interests")

else:
    file = st.file_uploader("Upload Resume", type=["pdf"])

    if file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        skills = extract_skills(text)
        interests = skills

        st.success("Detected Skills:")
        st.write(skills if skills else "No known skills detected")


if st.button("Analyze"):

    if not skills:
        st.warning("Provide skills or upload resume")
    else:
        response = requests.post(API_URL, json={
            "name": name,
            "skills": skills,
            "interests": interests,
            "education": education
        })

        result = response.json()

        st.subheader("🎯 Recommended Role")
        st.write(result["recommended_role"])

        if result["missing_skills"]:
            st.subheader("📌 Missing Skills")
            st.write(", ".join(result["missing_skills"]))

            st.subheader("🗺️ Roadmap")
            for step in result["roadmap"]:
                st.write("•", step)
