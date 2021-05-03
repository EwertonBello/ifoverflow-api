from typing import List, Optional
from pydantic import BaseModel


class Question(BaseModel):
    title:str
    description:str
    category_id:int

class ShowUser(BaseModel):
    name:str
    avatar:str
    class Config():
        orm_mode = True

class ShowBaseQuestion(BaseModel):
    title:str
    description:str
    votes:int
    user: ShowUser
    class Config():
        orm_mode = True

class ShowTag(BaseModel):
    id:int
    name:str
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

class ShowQuestion(ShowBaseQuestion):
    tags: List[ShowTag]
    # comments: List[ShowComment]
    # answers: List[ShowAnswer]
    class Config():
        orm_mode = True

class ShowTagWithQuestions(ShowTag):
    questions: List[ShowBaseQuestion]
    class Config():
        orm_mode = True

class ShowCategory(BaseModel):
    id:int
    name:str
    class Config():
        orm_mode = True

class ShowCategoryWithQuestions(ShowCategory):
    questions: List[ShowBaseQuestion]
    class Config():
        orm_mode = True
