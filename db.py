from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:Pa$$w0rd@localhost/db')

base = declarative_base()
class Menu(base):
    __tablename__ = "menus"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)

class SubMenu(base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)

class Dishes(base):
    __tablename__ = "dishes"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    submenu_id = Column(Integer, ForeignKey('submenus.id'), nullable=False)
