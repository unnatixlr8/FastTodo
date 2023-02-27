from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    title : str
    body : str

class ShowTodo(Todo):
    class Config():
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True