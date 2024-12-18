from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import get_password_hash, get_db, create_access_token, verify_password
from app.models import Teacher
from app.schemas.user_schema import *
from app.schemas.token_schema import Token

router = APIRouter()


@router.post("/register/teacher", response_model=Token)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(Teacher).filter(Teacher.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    db_user = db.query(Teacher).filter(Teacher.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = Teacher(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    access_token = create_access_token(data={"sub": new_user.username}, role="teacher", user_id=new_user.id)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login/teacher", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Teacher).filter(Teacher.username == form_data.username).first()
    if not user or not verify_password(form_data.password+user.salt, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username}, role="teacher", user_id=user.id)
    return {"access_token": access_token, "token_type": "bearer"}