from src.core.models.validator_model import SignInFormValidator
from src.core.models.url_model import URLModel
from src.core.models.session_model import SessionModel

from requests import get, post


class ModelController:
    def __init__(self):
        self.SessionModel = SessionModel()


    def sign_in(self, **kwargs):
        if SignInFormValidator().is_valid(**kwargs):
            response = post(
                url=URLModel().get_url(key='sign_in'),
                json=kwargs
            )
            if response.status_code == 200:
                self.SessionModel.set_session(session=response.json())

                try:
                    self.verify_session(authorization=self.SessionModel.get_access_token())
                except: pass

                return True
            else:
                # debería retornar una ventana de respuesta acá
                return False
    
    def verify_session(self, authorization: str):
        response = post(
            url=URLModel.get_url(key='verify_session').format(access_token=authorization),
            headers={'Authorization': f'Bearer {authorization}'}
        )

        print(f'Status: {response.status_code}')
        print(f'Body: {response.text}')
        return response
