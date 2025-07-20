from src.core.views.sign_in import SignInView
from src.core.views.application import ApplicationView

from typing import Union

from PySide6.QtWidgets import QLineEdit, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6 import QtCore




class ViewController:

    def __init__(self, parent):
        self.parent = parent

    
    
    def set_object_status(self, Object: Union[QLineEdit, QPushButton], status: bool):
        return Object.setEnabled(status)
    
    
    def get_sign_in_view(self):
        self.SignInView = SignInView()
        self.SignInView.setupUi()
        self.SignInView.setWindowTitle(self.SignInView.__str__())
        self.SignInView.setFocus()

        #self.SignInView.lineEditUsername.returnPressed.connect(
        #    lambda: self.parent.signIn(username=self.SignInView.lineEditUsername.text(), password=self.SignInView.lineEditPassword.text())
        #)
        
        self.SignInView.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
        #self.SignInView.lineEditPassword.returnPressed.connect(lambda: self.parent.signIn(username=self.SignInView.lineEditUsername.text(), password=self.SignInView.lineEditPassword.text()))
        
        self.SignInView.pushButtonSignIn.clicked.connect(
            lambda: self.parent.sign_in(username=self.SignInView.lineEditUsername.text(), password=self.SignInView.lineEditPassword.text())
        )
        self.SignInView.pushButtonSignIn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SignInView.setWindowState(QtCore.Qt.WindowActive)
        self.SignInView.raise_()

        return self.SignInView

        


    def swipe_sidebar(self, normal=44, extend=180, duration=250) -> None:
        width = self.ApplicationView.frameSidebar.width()

        if width == normal:
            extend = 180
        else:
            extend = normal

        self.animation = QPropertyAnimation(self.ApplicationView.frameSidebar, b'minimumWidth')
        self.animation.setDuration(duration)
        self.animation.setStartValue(width)
        self.animation.setEndValue(extend)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def get_application_view(self):
        self.ApplicationView = ApplicationView()
        self.ApplicationView.setupUi()
        self.ApplicationView.setWindowTitle('<Application>')
        self.ApplicationView.setFocus()
        self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageHome)
        self.ApplicationView.pushButtonSwipeSidebar.clicked.connect(lambda: self.swipe_sidebar())
        self.ApplicationView.pushButtonOperations.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageOperations))
        self.ApplicationView.pushButtonActions.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageActions))
        self.ApplicationView.pushButtonIndex.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageData))
        self.ApplicationView.pushButtonProfile.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageUsers))
        self.ApplicationView.pushButtonExit.clicked.connect(lambda: self.ApplicationView.close())

        self.ApplicationView.setWindowState(QtCore.Qt.WindowActive)
        self.ApplicationView.raise_()
        
        return self.ApplicationView