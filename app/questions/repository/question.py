from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.questions import models, schemas


def create(current_user_id:int, request: schemas.Question, db: Session):
    new_question = request.dict()
    new_question['user_id'] = current_user_id
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

def show(current_user:schemas.ShowUser, id: int, db: Session):
    current_user_id = current_user.id if current_user else 0

    _question = db.query(models.Question).filter(models.Question.id == id).first()
    if not _question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Question with the id {id} is not available")
    try:
        _question.my_vote = [vote.vote for vote in _question.my_votes if vote.user_id == current_user_id][0]
    except IndexError:
        pass

    for answer in _question.answers:
        try:
            answer.my_vote = [vote.vote for vote in answer.my_votes if vote.user_id == current_user_id][0]
        except IndexError:
            pass

    _question.is_owner = (current_user_id == _question.user_id)
    return _question

def search(query:str, db: Session):
    return f"search questions with {query}"

def vote_question(positive:bool=True, question_id: int, db: Session):
    vote = 1 if positive else (-1)
    try:
        db.execute(
            text('CALL votarNaPergunta(:question_id, :vote)'), 
            {'question_id': question_id, 'vote': vote}
        )
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Votes not update, check the request and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Voted successfully!")
