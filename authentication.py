from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, models, JWTToken
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"invalid credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"invalid credentials")
    
    #generate jwt token
    access_token = JWTToken.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}