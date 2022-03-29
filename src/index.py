from fastapi import APIRouter, status
from src.auth.router import router as auth_router
router = APIRouter()
router.include_router( router=auth_router, prefix="/auth")
@router.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "API Routes"
    }