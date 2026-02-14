from app.services.job_analyzer import recommend_role

def determine_role(skills, interests):
    return recommend_role(skills, interests)
