from pydantic import BaseModel
from typing import List, Optional

class ChoiceCreate(BaseModel):
    text: str
    is_correct: bool

class QuestionCreate(BaseModel):
    text: str
    choices: List[ChoiceCreate]

class QuizCreate(BaseModel):
    title: str
    description: Optional[str] = None
    questions: List[QuestionCreate]
