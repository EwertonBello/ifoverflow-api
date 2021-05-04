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

@router.post('/', status_code=201)
async def create_comment(request: Comment, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return "comment.create(current_user.id, request, db)"

@router.get('/{id}', response_model=ShowComment)
async def get_comment(id: int, db: Session = Depends(get_db)):
    return "comment.show(id, db)"
