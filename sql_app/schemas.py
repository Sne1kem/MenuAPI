from pydantic import BaseModel


class MenuBase(BaseModel):
    id: int
    title: str
    description: str


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: int

    class Config:
        orm_mode = True


class SubMenuBase(BaseModel):
    title: str
    description: str

class SubMenuCreate(SubMenuBase):
    pass


class SubMenu(SubMenuBase):
    id: int

    class Config:
        orm_mode = True


class DishesBase(BaseModel):
    title: str
    description: str


class DishesCreate(DishesBase):
    pass


class Dishes(DishesBase):
    id: int

    class Config:
        orm_mode = True
