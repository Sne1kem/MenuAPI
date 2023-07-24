from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete, update, join
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import menu, submenu, dishes
from .schema import MenuCreate, SubMenuCreate, DishCreate


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["menu"],

)

@router.get("/")
async def get_menus(session: AsyncSession = Depends(get_async_session)):
    query = select(menu)
    result = await session.execute(query)
    res = result.mappings().all()
    return res

@router.get("/{id}")
async def get_menu(id, session: AsyncSession = Depends(get_async_session)):
    query = select(menu).where(menu.c.id == id)
    result = await session.execute(query)
    res = result.mappings().all()
    query = select(submenu).where(submenu.c.menu_id == id)
    result = await session.execute(query)
    submenu_count = result.mappings().all()
    dishes_count = 0
    for i in submenu_count:
        query = select(dishes).where(dishes.c.submenu_id == i['id'])
        result = await session.execute(query)
        resi = len(result.mappings().all())
        dishes_count += resi
    submenus_count = len(submenu_count)
    try:
        res = dict(res[0])
    except:
        raise HTTPException(404, 'menu not found')
    res['submenus_count'] = submenus_count
    res['dishes_count'] = dishes_count
    try:
        if(res['id']):
            return res
    except:
        raise HTTPException(404, 'menu not found')

@router.post("/", status_code=201)
async def add_menu(new_menu: MenuCreate,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(menu).values(**new_menu.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(menu)
    result = await session.execute(query)
    res = result.mappings().all()[-1]
    return res

@router.delete("/{menu_id}")
async def del_menu(menu_id, session: AsyncSession = Depends(get_async_session)):
    query = delete(menu).where(menu.c.id == menu_id)
    await session.execute(query)
    await session.commit()
    return {'status': 'success'}

@router.patch("/{menu_id}", status_code=200)
async def update_menu(menu_id, new_data: MenuCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(menu).where(menu.c.id == menu_id).values(**new_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(menu).where(menu.c.id == menu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res[0])

@router.get("/{menu_id}/submenus")
async def get_submenus(menu_id,session: AsyncSession = Depends(get_async_session)):
    query = select(submenu).where(submenu.c.menu_id == menu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res)

@router.post("/{menu_id}/submenus", status_code=201)
async def add_submenu(menu_id, new_submenu: SubMenuCreate, session: AsyncSession = Depends(get_async_session)):
    new = new_submenu.dict()
    new.update({"menu_id": menu_id})
    stmt = insert(submenu).values(**new)
    await session.execute(stmt)
    await session.commit()
    query = select(submenu).where(submenu.c.menu_id == menu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res[0])

@router.get("/{menu_id}/submenus/{submenu_id}")
async def get_submenu(menu_id, submenu_id, session: AsyncSession = Depends(get_async_session)):
    query = select(submenu).where(submenu.c.menu_id == menu_id, submenu.c.id == submenu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    query = select(dishes).where(dishes.c.submenu_id == submenu_id)
    result = await session.execute(query)
    dishes_count = len(result.mappings().all())
    try:
        res = dict(res[0])
    except:
        raise HTTPException(404, 'submenu not found')
    res['dishes_count'] = dishes_count
    try:
        return res
    except:
        raise HTTPException(404, 'submenu not found')

@router.patch("/{menu_id}/submenus/{submenu_id}", status_code=200)
async def update_menu(menu_id, submenu_id, new_data: SubMenuCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(submenu).where(submenu.c.menu_id == menu_id, submenu.c.id == submenu_id).values(**new_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(submenu).where(submenu.c.menu_id == menu_id, submenu.c.id == submenu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res[0])

@router.delete("/{menu_id}/submenus/{submenu_id}", status_code=200)
async def del_submenu(menu_id, submenu_id, session: AsyncSession = Depends(get_async_session)):
    query = delete(submenu).where(submenu.c.menu_id == menu_id, submenu.c.id == submenu_id)
    await session.execute(query)
    await session.commit()
    return {'status': 'success'}

@router.get("/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(menu_id, submenu_id, session: AsyncSession = Depends(get_async_session)):
    query = select(dishes).where(dishes.c.submenu_id == submenu_id,)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res)

@router.post("/{menu_id}/submenus/{submenu_id}/dishes", status_code=201)
async def add_dish(menu_id, submenu_id, new_data: DishCreate, session: AsyncSession = Depends(get_async_session)):
    new = new_data.dict()
    new.update({"submenu_id": submenu_id})
    stmt = insert(dishes).values(**new)
    await session.execute(stmt)
    await session.commit()
    query = select(dishes).where(dishes.c.submenu_id == submenu_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res[0])

@router.get("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def get_submenu(menu_id, submenu_id, dish_id, session: AsyncSession = Depends(get_async_session)):
    query = select(dishes).where(dishes.c.submenu_id == submenu_id, dishes.c.id == dish_id)
    result = await session.execute(query)
    res = result.mappings().all()
    try:
        return res[0]
    except:
        raise HTTPException(404, 'dish not found')

@router.patch("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", status_code=200)
async def update_menu(menu_id, submenu_id, dish_id, new_data: DishCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = update(dishes).where(dishes.c.submenu_id == submenu_id, dishes.c.id == dish_id).values(**new_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(dishes).where(dishes.c.submenu_id == submenu_id, dishes.c.id == dish_id)
    result = await session.execute(query)
    res = result.mappings().all()
    return(res[0])

@router.delete("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", status_code=200)
async def del_submenu(menu_id, submenu_id, dish_id, session: AsyncSession = Depends(get_async_session)):
    query = delete(dishes).where(dishes.c.submenu_id == submenu_id, dishes.c.id == dish_id)
    await session.execute(query)
    await session.commit()
    return {'status': 'success'}