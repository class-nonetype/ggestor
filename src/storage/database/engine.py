from sqlalchemy import create_engine
from src.core.utils import DATABASE_URL

engine = create_engine(url=DATABASE_URL)

'''
with engine.connect() as connection:
    sql_statement = ''
    connection.execute(
        text(sql_statement)
    )
    connection.commit()
'''