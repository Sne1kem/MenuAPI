from pydantic import BaseModel
import uuid


class MenuCreate(BaseModel):
    title: str
    description: str

class SubMenuCreate(BaseModel):
    title: str
    description: str

class DishCreate(BaseModel):
    title: str
    description: str
    price: str
