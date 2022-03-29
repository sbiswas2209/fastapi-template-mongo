from sys import prefix
from fastapi import FastAPI, status
from src.index import router

app = FastAPI()

app.include_router(router=router, prefix="/api")

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "Server Started"
    }