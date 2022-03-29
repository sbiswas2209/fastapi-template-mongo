from fastapi import APIRouter, status

from src.auth.model import LoginRequestBody
from src.auth.service import loginUser
router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "Auth Routes"
    }

@router.post("/login", status_code=status.HTTP_200_OK)
def login(body: LoginRequestBody):
    result = loginUser(body)
    return {
        "message": body,
        "success": result
    }