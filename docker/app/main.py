from fastapi import FastAPI
from routers import items,name

app = FastAPI()

app.include_router(items.router)
app.include_router(name.router)