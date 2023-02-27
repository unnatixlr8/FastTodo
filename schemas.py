from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    title : str
    body : str

class TodoBase(Todo):
    class Config():
        orm_mode = True

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
    todos : List[TodoBase] = []
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None