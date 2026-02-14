from app.services.roadmap_generator import generate_roadmap

def generate_plan(role, missing_skills):
    return generate_roadmap(role, missing_skills)
