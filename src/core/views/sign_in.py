# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign-inMLJHTt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class SignInView(QMainWindow):
    def __init__(self):
        super(SignInView, self).__init__()
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            return self.close()
    

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(800, 460)
        self.setMinimumSize(QSize(800, 460))
        self.setMaximumSize(QSize(800, 460))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameContainer = QFrame(self.centralwidget)
        self.frameContainer.setObjectName(u"frameContainer")
        self.frameContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContainer.setFrameShadow(QFrame.Shadow.Plain)
        self.frameContainer.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frameContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frameForm = QFrame(self.frameContainer)
        self.frameForm.setObjectName(u"frameForm")
        self.frameForm.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameForm.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frameForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.labelUsername = QLabel(self.frameForm)
        self.labelUsername.setObjectName(u"labelUsername")
        self.labelUsername.setStyleSheet(u"QLabel {\n"
"	font: 300 14pt \"Microsoft YaHei UI Light\";\n"
"	color: #0f69b4;\n"
"}")

        self.gridLayout_3.addWidget(self.labelUsername, 1, 0, 1, 1)

        self.labelPassword = QLabel(self.frameForm)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"	font: 300 14pt \"Microsoft YaHei UI Light\";\n"
"	color: #0f69b4;\n"
"}")

        self.gridLayout_3.addWidget(self.labelPassword, 4, 0, 1, 1)

        self.lineEditUsername = QLineEdit(self.frameForm)
        self.lineEditUsername.setObjectName(u"lineEditUsername")
        self.lineEditUsername.setMinimumSize(QSize(0, 36))
        self.lineEditUsername.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid;\n"
"    border-color: #0f69b4;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    border-bottom-width: 5px;\n"
"    border-color: #0f69b4;\n"
"}\n"
"")
        self.lineEditUsername.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditUsername, 2, 0, 1, 1)

        self.lineEditPassword = QLineEdit(self.frameForm)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setMinimumSize(QSize(0, 36))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid;\n"
"    border-color: #0f69b4;\n"
"    font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"}\n"
"\n"
"QLineEdit:hover,\n"
"QLineEdit:focus {\n"
"    border-bottom-width: 5px;\n"
"    border-color: #0f69b4;\n"
"}\n"
"")
        self.lineEditPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEditPassword, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.pushButtonSignIn = QPushButton(self.frameForm)
        self.pushButtonSignIn.setObjectName(u"pushButtonSignIn")
        self.pushButtonSignIn.setMinimumSize(QSize(0, 46))
        self.pushButtonSignIn.setStyleSheet(u"QPushButton {\n"
"	background-color:  #E0701E;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 14pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon = QIcon()
        icon.addFile(u"src/assets/icons/24x24/cil-arrow-circle-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonSignIn.setIcon(icon)
        self.pushButtonSignIn.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.pushButtonSignIn, 7, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameForm, 0, 1, 1, 1)

        self.frameLabel = QFrame(self.frameContainer)
        self.frameLabel.setObjectName(u"frameLabel")
        self.frameLabel.setMinimumSize(QSize(420, 0))
        self.frameLabel.setMaximumSize(QSize(420, 16777215))
        self.frameLabel.setStyleSheet(u"QFrame {\n"
"	background-color: #222222;\n"
"}")
        self.frameLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLabel.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frameLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameContainer, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su nombre de usuario", None))
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su contrase\u00f1a", None))
        self.pushButtonSignIn.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

