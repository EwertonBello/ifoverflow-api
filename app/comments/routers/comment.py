from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.comments.repository import comment
from app.comments.schemas import ShowBaseComment, ShowCommentAnswer, ShowCommentQuestion, CommentAnswer, CommentQuestion
from app.users.schemas import User
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/comments",
    tags=['Comments']
)

get_db = database.get_db

@router.post('/answer', status_code=201, response_model=ShowBaseComment)
async def comment_answer(request: CommentAnswer, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return comment.comment_answer(current_user, request, db)

@router.post('/question', status_code=201, response_model=ShowBaseComment)
async def comment_question(request: CommentQuestion, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return comment.comment_question(current_user, request, db)

@router.get('/{id}/answer', response_model=ShowCommentAnswer)
async def get_comment_answer(id: int, db: Session = Depends(get_db)):
    return comment.show(False, id, db)

@router.get('/{id}/question', response_model=ShowCommentQuestion)
async def get_comment_question(id: int, db: Session = Depends(get_db)):
    return comment.show(True, id, db)
