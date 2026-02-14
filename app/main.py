from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.profile_agent import process_profile

app = FastAPI(title="Career Navigator AI")

class UserInput(BaseModel):
    name: str
    skills: str
    interests: str
    education: str

@app.get("/")
def home():
    return {"message": "Backend Running Successfully 🚀"}

@app.post("/analyze")
def analyze(user: UserInput):
    return process_profile(user)
