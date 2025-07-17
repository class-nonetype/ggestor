from src.core.views.sign_in import SignInView
from src.core.views.application import ApplicationView

from typing import Union

from PySide6.QtWidgets import QLineEdit, QPushButton
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6 import QtCore, QtWidgets


import pandas as pd
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




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




    def insert_test_data(self):
        # Crear DataFrames de prueba
        df1 = pd.DataFrame({
            'Categoria': ['A', 'B', 'C', 'D'],
            'Valor': [5, 10, 15, 20]
        })

        df2 = pd.DataFrame({
            'Categoria': ['E', 'F', 'G', 'H'],
            'Valor': [12, 22, 8, 30]
        })

        df3 = pd.DataFrame({
            'Categoria': ['I', 'J', 'K', 'L'],
            'Valor': [7, 17, 13, 27]
        })

        # Crear gráficos para cada DataFrame
        def create_bar_chart(df):
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.bar(df['Categoria'], df['Valor'], color='skyblue')
            ax.set_title('Gráfico de Barras')
            ax.set_xlabel('Categoría')
            ax.set_ylabel('Valor')
            return fig

        def create_pie_chart(df):
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.pie(df['Valor'], labels=df['Categoria'], autopct='%1.1f%%', startangle=90)
            ax.set_title('Gráfico de Tortas')
            return fig

        def create_line_chart(df):
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(df['Categoria'], df['Valor'], marker='o', color='orange')
            ax.set_title('Gráfico de Líneas')
            ax.set_xlabel('Categoría')
            ax.set_ylabel('Valor')
            return fig

        # Función para agregar un gráfico a un widget
        def add_chart_to_widget(widget: QWidget, fig):
            # Crear un layout vertical
            layout = QVBoxLayout()

            # Crear una etiqueta y agregarla al layout
            label = QLabel("Gráfico Generado")
            layout.addWidget(label)

            # Crear un canvas a partir de la figura y agregarlo al layout
            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

            # Establecer el layout al widget
            widget.setLayout(layout)

            # Dibujar el canvas
            canvas.draw()

        # Agregar gráficos a cada widget
        add_chart_to_widget(self.ApplicationView.widgetDataView1, create_bar_chart(df1))
        add_chart_to_widget(self.ApplicationView.widgetDataView2, create_pie_chart(df2))
        add_chart_to_widget(self.ApplicationView.widgetDataView3, create_line_chart(df3))

        # Ajustar el tamaño de los widgets si es necesario
        self.ApplicationView.widgetDataView1.setMinimumSize(400, 300)
        self.ApplicationView.widgetDataView2.setMinimumSize(400, 300)
        self.ApplicationView.widgetDataView3.setMinimumSize(400, 300)

    def get_application_view(self):
        self.ApplicationView = ApplicationView()
        self.ApplicationView.setupUi()
        self.ApplicationView.setWindowTitle('<Application>')
        self.ApplicationView.setFocus()
        self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageData)
        self.ApplicationView.pushButtonSwipeSidebar.clicked.connect(lambda: self.swipe_sidebar())
        self.ApplicationView.pushButtonOperations.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageOperations))
        self.ApplicationView.pushButtonActions.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageActions))
        self.ApplicationView.pushButtonIndex.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageData))
        self.ApplicationView.pushButtonProfile.clicked.connect(lambda: self.ApplicationView.stackedWidgetContent.setCurrentWidget(self.ApplicationView.pageUsers))
        self.ApplicationView.pushButtonExit.clicked.connect(lambda: self.ApplicationView.close())
        
        try:
            self.insert_test_data()
        except:
            pass

        self.ApplicationView.setWindowState(QtCore.Qt.WindowActive)
        self.ApplicationView.raise_()
        
        return self.ApplicationView