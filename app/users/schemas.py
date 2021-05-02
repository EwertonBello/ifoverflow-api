from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str
    avatar:str
    campus_id:int

class ShowRating(BaseModel):
    name:str
    description:str
    class Config():
        orm_mode = True

class ShowState(BaseModel):
    id:int
    name:str
    class Config():
        orm_mode = True

class ShowCampus(BaseModel):
    id:int
    name:str
    state: ShowState
    class Config():
        orm_mode = True

class ShowStateWithCampus(BaseModel):
    id:int
    name:str
    campus: List[ShowCampus]
    class Config():
        orm_mode = True

class ShowProfile(BaseModel):
    name:str
    avatar:str
    email:str
    rating: ShowRating
    campus: ShowCampus
    class Config():
        orm_mode = True

class ShowBaseUser(BaseModel):
    name:str
    avatar:str
    rating: ShowRating
    class Config():
        orm_mode = True

class ShowUser(ShowBaseUser):
    campus: ShowCampus
    class Config():
        orm_mode = True

class ShowCampusWithUsers(BaseModel):
    id:int
    name:str
    state: ShowState
    users: List[ShowBaseUser]
    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
