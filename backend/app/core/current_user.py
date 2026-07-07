from fastapi import Depends, HTTPException

from app.core.jwt import decode_access_token
from app.core.oauth2 import oauth2_scheme

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = decode_access_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token",
        )
        
    return payload["sub"]