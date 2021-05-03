from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.questions import models, schemas


def create(request: schemas.Question, db: Session):
    new_question = request.dict()
    try:
        db.execute(
            text('CALL perguntar(:title, :description, :category_id, :user_id)'), 
            new_question)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Question not created, check the request body and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Question created successfully!")

def get_all(db: Session):
    questions = db.query(models.Question).all()
    return questions

def show(id: int, db: Session):
    _question = db.query(models.Question).filter(models.Question.id == id).first()
    if not _question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Question with the id {id} is not available")
    return _question

def search(query:str, db: Session):
    return f"search questions with {query}"

def vote_question(question_id: int, db: Session):
    try:
        db.execute(text('CALL votarNaPergunta(:question_id)'), question_id)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Votes not update, check the request and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Voted successfully!")
