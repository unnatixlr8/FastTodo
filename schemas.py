from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    note : str

class TodoBase(Todo):
    class Config():
        orm_mode = True

class ShowTodo(Todo):
    class Config():
        orm_mode = True

class User(BaseModel):
    username : str
    password : str

class ShowUser(BaseModel):
    username:str
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
    username: Optional[str] = None