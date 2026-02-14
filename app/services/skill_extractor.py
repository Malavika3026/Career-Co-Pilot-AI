def extract_skills(text):
    return [skill.strip().lower() for skill in text.split(",")]
