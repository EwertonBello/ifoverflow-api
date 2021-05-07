from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.answers.repository import answer
from app.answers.schemas import ShowBaseAnswer, ShowAnswer, Answer
from app.users.schemas import User
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/answers",
    tags=['Answers']
)

get_db = database.get_db

@router.post('/', status_code=201, response_model=ShowBaseAnswer)
async def create_answer(request: Answer, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return answer.create(current_user, request, db)

@router.get('/{id}', response_model=ShowAnswer)
async def get_answer(id: int, db: Session = Depends(get_db)):
    return answer.show(id, db)

@router.put('/{id}/positive')
async def vote_positive(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return answer.vote_answer(True, id, db)

@router.put('/{id}/negative')
async def vote_negative(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return answer.vote_answer(False, id, db)

@router.put('/{id}/accept')
async def accept_answer(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return answer.accept_answer(current_user.id, id, db)
