from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.answers import models, schemas


def create(current_user: schemas.ShowUser, request: schemas.Answer, db: Session):
    new_answer = request.dict()
    new_answer['user_id'] = current_user.id
    try:
        db.execute(
            text('CALL responder(:description, :user_id, :question_id)'), 
            new_answer)
        db.commit()
        [answer_id] = db.execute('SELECT LAST_INSERT_ID() AS id').fetchone()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Answer not created, check the request body and try again")

    new_answer['id'] = answer_id
    new_answer['votes'] = 0
    new_answer['accepted'] = False
    new_answer['user'] = current_user
    return new_answer

def show(id: int, db: Session):
    _answer = db.query(models.Answer).filter(models.Answer.id == id).first()
    if not _answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Answer with the id {id} is not available")
    return _answer

def vote_answer(positive:bool, current_user_id: int, answer_id: int, db: Session):
    _answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    for my_vote in _answer.my_votes:
        if my_vote.user_id == current_user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="You can only vote once.")

    vote = 1 if positive else (-1)
    try:
        db.execute(
            text('CALL votarNaResposta(:user_id, :answer_id, :vote)'), 
            {'user_id': current_user_id, 'answer_id': answer_id, 'vote': vote}
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
    _answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if _answer.question.user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Accepted Answer unauthorized, check the request")

    for answer in _answer.question.answers:
        if answer.accepted:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Accepted Answer not update, an answer has already been accepted")

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
