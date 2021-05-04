from typing import List, Optional
from pydantic import BaseModel


class CommentAnswer(BaseModel):
    description:str
    answer_id:int

class CommentQuestion(BaseModel):
    description:str
    question_id:int

class ShowUser(BaseModel):
    name:str
    avatar:str
    class Config():
        orm_mode = True

class ShowAnswer(BaseModel):
    description:str
    votes:int
    accepted:bool
    user: ShowUser
    class Config():
        orm_mode = True

class ShowQuestion(BaseModel):
    title:str
    description:str
    votes:int
    user: ShowUser
    class Config():
        orm_mode = True

class ShowCommentAnswer(BaseModel):
    description:str
    user: ShowUser
    answer: ShowAnswer
    class Config():
        orm_mode = True

class ShowCommentQuestion(BaseModel):
    description:str
    user: ShowUser
    question: ShowQuestion
    class Config():
        orm_mode = True
