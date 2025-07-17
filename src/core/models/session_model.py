

class SessionModel:
    def __init__(self):
        self.session = None

    def set_session(self, session: dict):
        self.session = session

    def get_access_token(self):
        return self.session['accessToken']