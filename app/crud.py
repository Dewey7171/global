from sqlalchemy.orm import Session
from app import models, schemas

def create_quiz(db: Session, quiz_data: schemas.QuizCreate):
    quiz = models.Quiz(title=quiz_data.title, description=quiz_data.description)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    for question_data in quiz_data.questions:
        question = models.Question(text=question_data.text, quiz_id=quiz.id)
        db.add(question)
        db.commit()
        db.refresh(question)

        for choice_data in question_data.choices:
            choice = models.Choice(text=choice_data.text, is_correct=choice_data.is_correct, question_id=question.id)
            db.add(choice)
    
    db.commit()
    return quiz
