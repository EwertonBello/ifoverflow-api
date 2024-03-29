from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.comments import models, schemas


def comment_answer(current_user: schemas.ShowUser, request: schemas.CommentAnswer, db: Session):
    new_comment = request.dict()
    new_comment['user_id'] = current_user.id
    try:
        db.execute(
            text('CALL comentarResposta(:description, :user_id, :answer_id)'), 
            new_comment)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Comment not created, check the request body and try again")

    new_comment['user'] = {'id':current_user.id,'name':current_user.name,'avatar':current_user.avatar}
    return new_comment

def comment_question(current_user:schemas.ShowUser, request: schemas.CommentQuestion, db: Session):
    new_comment = request.dict()
    new_comment['user_id'] = current_user.id
    try:
        db.execute(
            text('CALL comentarPergunta(:description, :user_id, :question_id)'), 
            new_comment)
        db.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Comment not created, check the request body and try again")

    new_comment['user'] = {'id':current_user.id,'name':current_user.name,'avatar':current_user.avatar}
    return new_comment

def show(in_question: bool, id: int, db: Session):
    if in_question:
        _comment = db.query(models.Comments_Question).filter(models.Comments_Question.id == id).first()
    else:
        _comment = db.query(models.Comments_Answer).filter(models.Comments_Answer.id == id).first()

    if not _comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment with the id {id} is not available")
    return _comment
