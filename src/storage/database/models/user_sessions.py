from uuid import uuid4

from src.storage.database.base import base as Base


from sqlalchemy import (
    Column,
    DateTime,
    String
)
from sqlalchemy.dialects.postgresql import UUID



class UserSessions(Base):

    __tablename__ = 'user_sessions'

    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    client              = Column(String, nullable=False)
    session_date        = Column(DateTime, nullable=False)
    access_token        = Column(String, nullable=True)
