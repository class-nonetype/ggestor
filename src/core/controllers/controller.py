from src.core.controllers.view_controller import ViewController
from src.core.controllers.model_controller import ModelController

class Controller:
    def __init__(self):
        self.ViewController = ViewController(self)
        self.ModelController = ModelController()
    
    def sign_in(self, **kwargs):
        status = self.ModelController.sign_in(**kwargs)
        if status:
            self.get_application_view().show()

    def verify_session(self):
        try:
            return self.ModelController.verify_session(
                authorization=self.ModelController.SessionModel.get_access_token()
            ).status_code
        except:
            return self.ModelController.verify_session(
                authorization=self.ModelController.InternalDatabaseModel.select_session()
            ).status_code
    
    def get_sign_in_view(self):
        sign_in_view = self.ViewController.get_sign_in_view()
        return sign_in_view

    def get_application_view(self):
        application_view = self.ViewController.get_application_view()
        return application_view

    def get_view(self):
        if self.verify_session() == 200:
            application_view = self.ViewController.get_application_view()
            application_view.show()
        else:
            sign_in_view = self.ViewController.get_sign_in_view()
            sign_in_view.show()

            

def run_application() -> None:
    return Controller().get_view()
