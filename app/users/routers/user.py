from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import user
from app.users.schemas import User, ShowUser, ShowProfile
from app.users import oauth2
from app import database

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=201)
async def register_user(request: User, db: Session = Depends(get_db)):
    return user.register(request, db)

@router.get('/{id}', response_model=ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get('/profile/', response_model=ShowProfile)
async def get_profile(current_user: User = Depends(oauth2.get_current_user)):
    return current_user