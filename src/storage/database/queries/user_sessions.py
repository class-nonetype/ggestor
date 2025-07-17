from sqlalchemy.orm.session import Session
from sqlalchemy import and_, desc

from src.storage.database.models.user_sessions import UserSessions

def insert_user_session(database: Session, **kwargs):
    user_session = UserSessions(**kwargs)

    database.add(user_session)
    database.commit()
    database.refresh(user_session)

    return True

def select_user_session(database: Session):
    user_session = database.query(UserSessions).order_by(desc(UserSessions.session_date)).first()
    return user_session.access_token if user_session else 404