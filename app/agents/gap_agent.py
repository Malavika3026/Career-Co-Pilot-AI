from app.services.job_analyzer import get_top_skills_for_role

def identify_skill_gap(user_skills, role):

    user_skills_list = [
        s.strip().lower() for s in user_skills.split(",")
    ]

    top_skills = get_top_skills_for_role(role)

    missing = [
        skill for skill in top_skills
        if skill.lower() not in user_skills_list
    ]

    return missing
