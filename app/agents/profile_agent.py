from app.agents.role_agent import determine_role
from app.agents.gap_agent import identify_skill_gap
from app.agents.planner_agent import generate_plan

def process_profile(user):

    role = determine_role(user.skills, user.interests)

    gap = identify_skill_gap(user.skills, role)

    roadmap = generate_plan(role, gap)

    return {
        "recommended_role": role,
        "missing_skills": gap,
        "roadmap": roadmap
    }
