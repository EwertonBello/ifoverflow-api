from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
# from app.comments.repository import comment
from app.comments.schemas import ShowComment, Comment
from app.users.schemas import User
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/comments",
    tags=['Comments']
)

get_db = database.get_db

@router.post('/answer', status_code=201)
async def comment_answer(request: Comment, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return "comment.comment_answer(current_user.id, request, db)"

@router.post('/question', status_code=201)
async def comment_question(request: Comment, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return "comment.comment_question(current_user.id, request, db)"

@router.get('/{id}/answer', response_model=ShowComment)
async def get_comment_answer(id: int, db: Session = Depends(get_db)):
    return "comment.show('answer', id, db)"

@router.get('/{id}/question', response_model=ShowComment)
async def get_comment_question(id: int, db: Session = Depends(get_db)):
    return "comment.show('question', id, db)"
