from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

item_list = []


class Item(BaseModel):
    name: str


@router.get("/items")
def get_items():
    return {"items": item_list}


@router.post("/items", status_code=201)
def create_item(item: Item):
    item_list.append(item.name)
    return {"items": item_list}
