from src.core.utils import DATABASE_URL

class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None
