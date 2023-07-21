from sqlalchemy.orm import Session

from . import models, schemas


def get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()

def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(**menu.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def get_submenu(db: Session, submenu_id: int):
    return db.query(models.SubMenu).filter(models.SubMenu.id == submenu_id).first()

def create_submenu(db: Session, submenu: schemas.SubMenuCreate):
    db_submenu = models.Menu(**submenu.dict())
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu

def get_dishes(db: Session, dish_id: int):
    return db.query(models.Dishes).filter(models.Dishes.id == dish_id).first()

def create_dishes(db: Session, dishes: schemas.DishesCreate):
    db_dishes = models.Menu(**dishes.dict())
    db.add(db_dishes)
    db.commit()
    db.refresh(db_dishes)
    return db_dishes