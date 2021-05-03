from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.answers.repository import answers
from app.answers.schemas import ShowAnswer, Answer
from app.users.schemas import User
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/answers",
    tags=['Answers']
)

get_db = database.get_db

@router.post('/', status_code=201)
async def create_answer(request: Answer, db: Session = Depends(get_db)):
    return answers.create(request, db)

@router.get('/{id}', response_model=ShowAnswer)
async def get_answer(id: int, db: Session = Depends(get_db)):
    return answers.show(id, db)

@router.put('/{id}')
async def vote_answer(id: int, db: Session = Depends(get_db)):
    return answers.vote_answer(id, db)

@router.put('/{id}')
async def accept_answer(id: int, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return answers.accept_answer(current_user.id, id, db)
