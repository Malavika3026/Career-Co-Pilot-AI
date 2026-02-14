def generate_roadmap(role, missing_skills):

    roadmap = []

    for skill in missing_skills:
        roadmap.append(f"Learn {skill}")

    roadmap.extend([
        "Build 2-3 projects",
        "Improve resume",
        "Prepare for interviews",
        "Start applying"
    ])

    return roadmap
