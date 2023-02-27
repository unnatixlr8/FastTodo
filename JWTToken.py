from datetime import datetime, timedelta
from jose import JWSError, jwt, JWTError
from typing import Union
import schemas


SECRET_KEY = "12f71daacedaa6f030779e2daa567ad8ebe20cc964b924519901d0e0ebe7771e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
