from fastapi import FastAPI
from app.routes import quiz

app = FastAPI()

app.include_router(quiz.router, prefix="/api", tags=["quiz"])
