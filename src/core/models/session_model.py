

class SessionModel:
    def __init__(self):
        self.session = None

    def set_session(self, session: dict) -> None:
        self.session = session

    def get_access_token(self) -> str:
        return self.session['accessToken']