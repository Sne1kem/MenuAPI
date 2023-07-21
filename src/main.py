from fastapi import Body, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from pydantic import BaseModel, Field
import databases

from restaurant.router import router as router_restaurant


app = FastAPI()

app.include_router(router_restaurant)
