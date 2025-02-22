from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import QuizCreate
from app.crud import create_quiz

router = APIRouter()

@router.post("/quizzes/")
async def create_quiz_api(quiz: QuizCreate, db: AsyncSession = Depends(get_db)):
    return await create_quiz(db, quiz)
