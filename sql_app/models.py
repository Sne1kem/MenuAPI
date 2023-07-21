from sqlalchemy import Integer, String, Column, ForeignKey, MetaData

from .db import Base



class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)

class SubMenu(Base):
    __tablename__ = "submenus"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)

class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    submenu_id = Column(Integer, ForeignKey('submenus.id'), nullable=False)