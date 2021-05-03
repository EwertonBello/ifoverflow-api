from typing import List, Optional
from pydantic import BaseModel


class Answer(BaseModel):
    description:str
    votes:int
    accepted:bool
    user_id:int
    question_id:int

class ShowUser(BaseModel):
    name:str
    avatar:str
    class Config():
        orm_mode = True

class ShowComment(BaseModel):
    description:str
    user: ShowUser
    class Config():
        orm_mode = True

class ShowAnswer(BaseModel):
    description:str
    votes:int
    accepted:bool
    user: ShowUser
    class Config():
        orm_mode = True
