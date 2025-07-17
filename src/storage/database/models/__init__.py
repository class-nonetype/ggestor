# Registros

from src.storage.database.base import base as Base
from src.storage.database.engine import engine as Engine

from src.storage.database.models.user_sessions import UserSessions


from sqlalchemy import inspect
from sqlalchemy.orm import clear_mappers


# Bloque de creación de los modelos
try:
    Base.metadata.create_all(bind=Engine)
except Exception as exception:
    raise exception
