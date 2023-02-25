from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'author': {'name': 'Unnati'}}

@app.get('/about')
def about():
    return {'data': 'This app is made using FastAPI and Python by Unnati Gupta'}
