from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

items = []


class Item(BaseModel):
    name: str


@router.get("/items")
def get_items():
    return {"items": items}


@router.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return {"items": items}
