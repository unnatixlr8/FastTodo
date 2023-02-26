from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import Optional
import uvicorn
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/')
def index():
    return {'author': {'name': 'Unnati'}}


@app.get('/about')
def about():
    return {'data': 'This app is made using FastAPI and Python by Unnati Gupta'}


# @app.get('/todo')
# def todo(limit = 10, published: bool = True, sort: Optional[str] = None):
#     if published:
#         return {'data': f'{limit} published from the db'}
#     else:
#         return {'data': f'{limit} unpublished todos from the db'}

@app.get('/todo')
def all(db: Session = Depends(get_db)):
    todo_list = db.query(models.Todo).all()
    return todo_list

    

# @app.get('/todo/draft')
# def draft():
#     return {'data':'unpublished'}


@app.get('/todo/{id}', status_code=status.HTTP_200_OK)
def show(id, response: Response, db: Session = Depends(get_db)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item {id} not found")
    return todo_list

@app.post('/todo', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Todo, db: Session = Depends(get_db)):
    new_todo = models.Todo(title=request.title, body=request.body)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.delete('/todo/{id}', status_code=status.HTTP_200_OK)
def delete(id, db:Session = Depends(get_db)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo_list.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {id} not found")
    todo_list.delete(synchronize_session=False)
    db.commit()
    return {'detail' : f"Todo {id} deleted"}

@app.put('/todo/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Todo, db:Session = Depends(get_db)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo_list.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Todo {id} not found")
    todo_list.update(request.dict())
    db.commit()
    return {"detail": f"Todo {id} updated"}

#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=9000)