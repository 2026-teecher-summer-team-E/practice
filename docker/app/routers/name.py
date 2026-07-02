# APIRouter에서 fastapi라는 것에 대한 문법을 받아오겠다.
from fastapi import APIRouter  

router = APIRouter()

@router.get("/yeji")
def get_users():
    return {"장예지 입니다."}