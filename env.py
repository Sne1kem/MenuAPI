from os import environ
from alembic import context
from models import dishes, submenus, menus

config  = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_USER", "fastapi_user")
config.set_section_option(section, "DB_PASS", "fastapi_pass")
config.set_section_option(section, "DB_NAME", "fastapi_name")
config.set_section_option(section, "DB_HOST", "fastapi_host")

fileConfig(config.config_file_name)

target_metadata = [menus.metadata, submenus.metadata, dishes.metadata]