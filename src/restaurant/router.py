from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import menu
from .schema import MenuCreate


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["menu"],

)

@router.get("/")
async def get_menus(session: AsyncSession = Depends(get_async_session)):
    query = select(menu)
    result = await session.execute(query)
    return result.scalars().all()

@router.get("/{id}")
async def get_menu(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(menu).where(menu.c.id == id)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/", status_code=201)
async def add_menu(new_menu: MenuCreate,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(menu).values(**new_menu.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}

@router.delete("/{id}")
async def del_menu(menu_id ,session: AsyncSession = Depends(get_async_session)):
    stmt = delete(menu).where(menu.c.id == menu_id)
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}