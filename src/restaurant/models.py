from sqlalchemy import MetaData, UUID, String, Column, ForeignKey, Table, Float
import uuid

metadata = MetaData()

menu = Table(
    "menu",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
)

submenu = Table(
    "submenu",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("menu_id", UUID, ForeignKey(menu.c.id, ondelete="cascade"))
)

dishes = Table(
    "dish",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
    Column("price", String, nullable=False),
    Column("submenu_id", UUID, ForeignKey(submenu.c.id, ondelete="cascade"))
)

