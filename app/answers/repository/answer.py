from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.answers import models, schemas


def create(request: schemas.Answer, db: Session):
    return "create answer"
    new_answer = request.dict()
    try:
        db.execute(
            text('CALL responder(:description, :user_id, :question_id)'), 
            new_answer)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Answer not created, check the request body and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Answer created successfully!")

def show(id: int, db: Session):
    return "show answer"
    _answer = db.query(models.Answer).filter(models.Answer.id == id).first()
    if not _answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Answer with the id {id} is not available")
    return _answer

def vote_answer(answer_id: int, db: Session):
    return "vote_answer"
    try:
        db.execute(
            text('CALL votarNaResposta(:answer_id)'), 
            {'answer_id': answer_id}
        )
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Votes not update, check the request and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Voted successfully!")

def accept_answer(current_user_id: int, answer_id: int, db: Session):
    """Se o dono da pergunta for o current user, permite isso"""
    _answer = db.query(models.Answer).filter(models.Answer.id == id).first()
    print(_answer)
    print(_answer.question.user_id)
    if _answer.question.user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Accepted Answer unauthorized, check the request")
    print("point1")
    return "vote_answer"
    try:
        db.execute(
            text('CALL atualizarParaMelhorResposta(:answer_id)'), 
            {'answer_id': answer_id}
        )
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Accepted Answer not update, check the request and try again")

    return HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Accepted Answer successfully!")
