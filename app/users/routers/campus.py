from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.users.repository import campus
from app.users.schemas import ShowCampus, ShowUser
from app import database

router = APIRouter(
    prefix="/campus",
    tags=['Campus']
)

get_db = database.get_db

@router.get('/', response_model=List[ShowCampus])
async def get_campus_list(db: Session = Depends(get_db)):
    return campus.get_all(db)

@router.get('/{id}', response_model=ShowCampus)
async def get_campus(id: int, db: Session = Depends(get_db)):
    return campus.show(id, db)

@router.get('/{id}/users', response_model=List[ShowUser])
async def get_users_by_campus(id: int, db: Session = Depends(get_db)):
    return campus.users_by_campus(id, db)
