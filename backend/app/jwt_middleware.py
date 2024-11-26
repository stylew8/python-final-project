import jwt
from fastapi import Request, HTTPException
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from app.auth import SECRET_KEY, ALGORITHM
from app.models import User
from sqlalchemy.orm import Session
from app.database import SessionLocal

# Middleware для проверки JWT токенов
class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Пропускаем аутентификацию для некоторых эндпоинтов
        if request.url.path in ["/token", "/register"]:
            return await call_next(request)

        # Получаем токен из заголовка Authorization
        auth_header = request.headers.get("Authorization")
        if auth_header is None or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Authorization header missing or invalid")

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")
            
            # Проверяем существование пользователя в базе данных
            db: Session = SessionLocal()
            user = db.query(User).filter(User.username == username).first()
            db.close()

            if user is None:
                raise HTTPException(status_code=401, detail="User not found")

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

        response = await call_next(request)
        return response
