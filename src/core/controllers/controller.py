from src.core.controllers.view_controller import ViewController
from src.core.controllers.model_controller import ModelController

class Controller:
    def __init__(self):
        self.ViewController = ViewController(self)
        self.ModelController = ModelController()
    
    def sign_in(self, **kwargs):
        status = self.ModelController.sign_in(**kwargs)
        return None if not status else self.get_view(mode=False)

    def get_view(self, **kwargs):
        if kwargs['mode']:

            sign_in_view = self.ViewController.get_sign_in_view(mode=True)
            #self.ViewController.set_object_status(sign_in_view.pushButtonSignIn, False)
            sign_in_view.show()

        else:
            application_view = self.ViewController.get_application_view()
            application_view.show()


def run_application():
    return Controller().get_view(mode=True)
