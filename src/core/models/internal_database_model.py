from src.storage.database.session import connection
from src.storage.database.queries.user_sessions import (
    insert_user_session,
    select_user_session
)
from uuid import uuid4
from datetime import datetime

class InternalDatabaseModel:
    def __init__(self):
        self.connection = connection
    
    def select_session(self):
        return select_user_session(database=self.connection)

    def insert_session(self, session: dict):

        insert_user_session(
            database=self.connection,
            id=uuid4(),
            client=session['client'],
            session_date=datetime.strptime(
                session['date'].replace(' PM', '').replace(' AM', ''), "%y/%m/%d %H:%M:%S"),
            access_token=session['accessToken']
        )