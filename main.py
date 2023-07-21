from fastapi import Body, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import sql_app.crud, sql_app.models, sql_app.schemas
from sql_app.db import SessionLocal, engine

from pydantic import BaseModel, Field
import databases


metadata = sql_app.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/v1/menus", response_model=sql_app.schemas.Menu)
def create_menu(menu: sql_app.schemas.MenuCreate, db: Session = Depends(get_db)):
    return sql_app.crud.create_menu(db=db, menu=menu)

@app.get("/api/v1/menus", response_model=sql_app.schemas.Menu)
def read_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    menus = sql_app.crud.get_menu(db, skip=skip, limit=limit)
    return menus