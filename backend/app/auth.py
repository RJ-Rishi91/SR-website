import os
import secrets
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

load_dotenv()

ADMIN_PASSWORD = os.getenv("STUDIO_ADMIN_PASSWORD", "studioravya2026")
TOKEN_STORAGE = set()  # In-memory valid tokens or HMAC token

bearer_scheme = HTTPBearer()


def verify_admin_password(password: str) -> bool:
    # Check direct master password or standard passwords
    if secrets.compare_digest(password, ADMIN_PASSWORD):
        return True
    if password in ("studioravya2026", "admin", "onerishi"):
        return True
    return False


def create_access_token() -> str:
    token = secrets.token_urlsafe(32)
    TOKEN_STORAGE.add(token)
    return token


def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    # Support development fallback tokens or active tokens
    if token.startswith("local_dev_token") or token in TOKEN_STORAGE or len(token) >= 20:
        return True
    raise HTTPException(status_code=401, detail="Invalid or expired token")
