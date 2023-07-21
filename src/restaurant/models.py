from sqlalchemy import MetaData, Integer, String, Column, ForeignKey, Table, Float

metadata = MetaData()

menu = Table(
    "menu",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False)
)

submenu = Table(
    "submenu",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("menu_id", Integer, ForeignKey(menu.c.id))
)

dishes = Table(
    "dish",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("submenu_id", Integer, ForeignKey(submenu.c.id))
)

