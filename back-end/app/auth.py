from datetime import datetime, timedelta
import jwt
from fastapi import Depends, HTTPException, status
from .models import User
from .config import Config

JWT_SECRET_KEY = Config.SECRET_KEY

def token_required(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user = User.query.filter_by(id=payload["user_id"]).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def create_access_token(user: User):
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token
