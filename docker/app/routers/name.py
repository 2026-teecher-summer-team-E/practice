from fastapi import APIRouter

router = APIRouter()

@router.get("/abcde")
def get_users():
    return {"이동호입니다."}