import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

try:
    job_postings = pd.read_csv(os.path.join(DATA_DIR, "job_postings.csv"))
    job_skills = pd.read_csv(os.path.join(DATA_DIR, "job_skills.csv"))

    job_postings.columns = job_postings.columns.str.lower().str.strip()
    job_skills.columns = job_skills.columns.str.lower().str.strip()

    print("Datasets loaded successfully")

except Exception as e:
    print("Dataset loading failed:", e)
    job_postings = pd.DataFrame()
    job_skills = pd.DataFrame()


def get_top_skills_for_role(role_name, top_n=10):

    if job_postings.empty or job_skills.empty:
        return []

    filtered_jobs = job_postings[
        job_postings["title"].str.lower() == role_name.lower()
    ]

    if filtered_jobs.empty:
        return []

    job_ids = filtered_jobs["job_id"].tolist()

    relevant_skills = job_skills[
        job_skills["job_id"].isin(job_ids)
    ]

    if relevant_skills.empty:
        return []

    skill_counts = relevant_skills["skill_abr"].value_counts()

    return skill_counts.head(top_n).index.tolist()


def recommend_role(user_skills: str, interests: str):

    if job_postings.empty:
        return "Data Scientist"

    user_skills_list = [
        s.strip().lower() for s in user_skills.split(",")
    ]

    role_scores = {}

    unique_roles = job_postings["title"].unique()

    for role in unique_roles:

        top_skills = get_top_skills_for_role(role)

        if not top_skills:
            continue

        match_count = sum(
            1 for skill in top_skills
            if skill.lower() in user_skills_list
        )

        role_scores[role] = match_count

    if not role_scores:
        return "Data Scientist"

    best_role = max(role_scores, key=role_scores.get)

    return best_role
