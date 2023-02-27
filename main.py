from fastapi import FastAPI, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from typing import Optional
import uvicorn
import schemas, models, authentication, oauth2
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from hashing import Hash


app = FastAPI(
    title = "FastTodo",
    description= "A Todo App made using FastApi and Python"
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)

@app.get("/", tags=['Backend Stuff'])
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get('/todo', tags=['Todo'])
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    todo_list = db.query(models.Todo).filter(models.Todo.user_id == get_current_user.id).all()
    return todo_list


@app.get('/todo/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowTodo, tags=['Todo'])
def show(id, response: Response, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item {id} not found")
    return todo_list

@app.post('/todo', status_code=status.HTTP_201_CREATED, tags=['Todo'])
def create(request: schemas.Todo, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_todo = models.Todo(note=request.note, user_id = get_current_user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.delete('/todo/{id}', status_code=status.HTTP_200_OK, tags=['Todo'])
def delete(id, db:Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo_list.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {id} not found")
    todo_list.delete(synchronize_session=False)
    db.commit()
    return {'detail' : f"Todo {id} deleted"}

@app.put('/todo/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Todo'])
def update(id: int, request:schemas.Todo, db:Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    todo_list = db.query(models.Todo).filter(models.Todo.id == id)
    if not todo_list.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Todo {id} not found")
    todo_list.update(request.dict())
    db.commit()
    return {"detail": f"Todo {id} updated"}


@app.post('/user', tags=['User'])
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    
    new_user = models.User(username=request.username, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
def get_user(id: int, db:Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with {id} not found")
    return user
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=9000)