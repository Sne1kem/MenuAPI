from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
import databases
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Pa$$w0rd@localhost/db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
class Menu(BaseModel):
    title: str
    description: str


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/v1/menus/")
async def create_menu(menu: Menu):
    return menu