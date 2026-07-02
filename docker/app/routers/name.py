from fastapi import APIRouter

router = APIRouter()

@router.get("/abcde")
def get_users():
    return {"이동호입니다."}
@router.get("/chaeyeon")
def get_users():
    return {"박채연입니다"}
