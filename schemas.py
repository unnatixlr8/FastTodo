from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    title : str
    body : str
