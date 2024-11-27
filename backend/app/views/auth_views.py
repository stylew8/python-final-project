from fastapi import APIRouter, Depends, HTTPException, Header, status
from app.auth import SECRET_KEY, ALGORITHM, oauth2_scheme
import jwt

router = APIRouter()

@router.get("/verify-token")
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        return {"valid": True, "username": payload.get("sub")}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
def verify_token_function(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Authorization token is missing")
    
    token = authorization.split(" ")[1] if " " in authorization else authorization
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    