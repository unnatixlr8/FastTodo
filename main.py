from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'author': {'name': 'Unnati'}}


@app.get('/about')
def about():
    return {'data': 'This app is made using FastAPI and Python by Unnati Gupta'}


@app.get('/todo')
def todo(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published from the db'}
    else:
        return {'data': f'{limit} unpublished todos from the db'}
    

@app.get('/todo/draft')
def draft():
    return {'data':'unpublished'}


@app.get('/todo/{id}')
def show(id: int):
    return {'todo': id}

@app.post('/todo')
def create_todo():
    return {'data': 'Post is created'}