from fastapi import APIRouter

router = APIRouter()

@router.get("/chaeyeon")
def get_users():
    return {"박채연입니다"}