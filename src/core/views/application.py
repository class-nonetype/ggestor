
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QTreeWidget, QWidget)


class ApplicationView(QMainWindow):
    def __init__(self):
        super(ApplicationView, self).__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            return self.close()
    

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(860, 580)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameContainer = QFrame(self.centralwidget)
        self.frameContainer.setObjectName(u"frameContainer")
        self.frameContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContainer.setFrameShadow(QFrame.Shadow.Plain)
        self.frameContainer.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frameContainer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameSidebar = QFrame(self.frameContainer)
        self.frameSidebar.setObjectName(u"frameSidebar")
        self.frameSidebar.setMinimumSize(QSize(44, 0))
        self.frameSidebar.setMaximumSize(QSize(0, 16777215))
        self.frameSidebar.setStyleSheet(u"QFrame {\n"
"	/* E0701E, D27B3C*/\n"
"	background-color:  #E0701E;\n"
"	border: 0;\n"
"}")
        self.frameSidebar.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSidebar.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSidebar.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frameSidebar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSwipeSidebar = QPushButton(self.frameSidebar)
        self.pushButtonSwipeSidebar.setObjectName(u"pushButtonSwipeSidebar")
        self.pushButtonSwipeSidebar.setMinimumSize(QSize(0, 46))
        self.pushButtonSwipeSidebar.setStyleSheet(u"QPushButton {\n"
"	background-color:  #E0701E;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../icons/24x24/cil-list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonSwipeSidebar.setIcon(icon)
        self.pushButtonSwipeSidebar.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonSwipeSidebar, 0, 0, 1, 1)

        self.pushButtonIndex = QPushButton(self.frameSidebar)
        self.pushButtonIndex.setObjectName(u"pushButtonIndex")
        self.pushButtonIndex.setMinimumSize(QSize(0, 46))
        self.pushButtonIndex.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../icons/24x24/cil-home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonIndex.setIcon(icon1)
        self.pushButtonIndex.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonIndex, 2, 0, 1, 1)

        self.pushButtonProfile = QPushButton(self.frameSidebar)
        self.pushButtonProfile.setObjectName(u"pushButtonProfile")
        self.pushButtonProfile.setMinimumSize(QSize(0, 46))
        self.pushButtonProfile.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../icons/24x24/cil-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonProfile.setIcon(icon2)
        self.pushButtonProfile.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonProfile, 8, 0, 1, 1)

        self.pushButtonActions = QPushButton(self.frameSidebar)
        self.pushButtonActions.setObjectName(u"pushButtonActions")
        self.pushButtonActions.setMinimumSize(QSize(0, 46))
        self.pushButtonActions.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../icons/24x24/cil-touch-app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonActions.setIcon(icon3)
        self.pushButtonActions.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonActions, 5, 0, 1, 1)

        self.pushButtonOperations = QPushButton(self.frameSidebar)
        self.pushButtonOperations.setObjectName(u"pushButtonOperations")
        self.pushButtonOperations.setMinimumSize(QSize(0, 46))
        self.pushButtonOperations.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #D27B3C;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../icons/24x24/cil-library.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOperations.setIcon(icon4)
        self.pushButtonOperations.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonOperations, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.pushButtonExit = QPushButton(self.frameSidebar)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        self.pushButtonExit.setMinimumSize(QSize(0, 46))
        self.pushButtonExit.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	border: 0;\n"
"	border-color: transparent;\n"
"	font: 300 12pt \"Microsoft YaHei UI Light\";\n"
"	color: #FFFFFF;\n"
"    border-radius: 0;\n"
"    border-style: none;\n"
"	text-align: left; \n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c64b30;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../icons/24x24/cil-x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonExit.setIcon(icon5)
        self.pushButtonExit.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pushButtonExit, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 10, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameSidebar, 0, 0, 1, 1)

        self.stackedWidgetContent = QStackedWidget(self.frameContainer)
        self.stackedWidgetContent.setObjectName(u"stackedWidgetContent")
        self.stackedWidgetContent.setLineWidth(0)
        self.pageProfile = QWidget()
        self.pageProfile.setObjectName(u"pageProfile")
        self.gridLayout_9 = QGridLayout(self.pageProfile)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 3, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 0, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_11, 5, 0, 1, 1)

        self.frameUsersContent = QFrame(self.pageProfile)
        self.frameUsersContent.setObjectName(u"frameUsersContent")
        self.frameUsersContent.setMinimumSize(QSize(0, 400))
        self.frameUsersContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameUsersContent.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_9.addWidget(self.frameUsersContent, 4, 0, 1, 1)

        self.labelIndexTitle_2 = QLabel(self.pageProfile)
        self.labelIndexTitle_2.setObjectName(u"labelIndexTitle_2")
        self.labelIndexTitle_2.setStyleSheet(u"QLabel {\n"
"	font: 300 22pt \"Microsoft YaHei UI Light\";\n"
"	color: #E0701E;\n"
"}")

        self.gridLayout_9.addWidget(self.labelIndexTitle_2, 1, 0, 1, 1)

        self.frameLine_4 = QFrame(self.pageProfile)
        self.frameLine_4.setObjectName(u"frameLine_4")
        self.frameLine_4.setMinimumSize(QSize(0, 10))
        self.frameLine_4.setMaximumSize(QSize(16777215, 10))
        self.frameLine_4.setStyleSheet(u"QFrame {\n"
"	background-color: #D27B3C;\n"
"}")
        self.frameLine_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frameLine_4.setFrameShadow(QFrame.Shadow.Plain)
        self.frameLine_4.setLineWidth(0)

        self.gridLayout_9.addWidget(self.frameLine_4, 2, 0, 1, 1)

        self.stackedWidgetContent.addWidget(self.pageProfile)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.gridLayout_15 = QGridLayout(self.pageHome)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frameHomeContent = QFrame(self.pageHome)
        self.frameHomeContent.setObjectName(u"frameHomeContent")
        self.frameHomeContent.setMinimumSize(QSize(0, 400))
        self.frameHomeContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameHomeContent.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_15.addWidget(self.frameHomeContent, 2, 0, 1, 1)

        self.frameLine = QFrame(self.pageHome)
        self.frameLine.setObjectName(u"frameLine")
        self.frameLine.setMinimumSize(QSize(0, 10))
        self.frameLine.setMaximumSize(QSize(16777215, 10))
        self.frameLine.setStyleSheet(u"QFrame {\n"
"	background-color: #D27B3C;\n"
"}")
        self.frameLine.setFrameShape(QFrame.Shape.NoFrame)
        self.frameLine.setFrameShadow(QFrame.Shadow.Plain)
        self.frameLine.setLineWidth(0)

        self.gridLayout_15.addWidget(self.frameLine, 1, 0, 1, 1)

        self.labelHome = QLabel(self.pageHome)
        self.labelHome.setObjectName(u"labelHome")
        self.labelHome.setStyleSheet(u"QLabel {\n"
"	font: 300 22pt \"Microsoft YaHei UI Light\";\n"
"	color: #E0701E;\n"
"}")

        self.gridLayout_15.addWidget(self.labelHome, 0, 0, 1, 1)

        self.stackedWidgetContent.addWidget(self.pageHome)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 300 22pt \"Microsoft YaHei UI Light\";\n"
"	color: #E0701E;\n"
"}")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.frameLine_2 = QFrame(self.page)
        self.frameLine_2.setObjectName(u"frameLine_2")
        self.frameLine_2.setMinimumSize(QSize(0, 10))
        self.frameLine_2.setMaximumSize(QSize(16777215, 10))
        self.frameLine_2.setStyleSheet(u"QFrame {\n"
"	background-color: #D27B3C;\n"
"}")
        self.frameLine_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameLine_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frameLine_2.setLineWidth(0)

        self.gridLayout_4.addWidget(self.frameLine_2, 1, 0, 1, 1)

        self.frameActionsContent_2 = QFrame(self.page)
        self.frameActionsContent_2.setObjectName(u"frameActionsContent_2")
        self.frameActionsContent_2.setMinimumSize(QSize(0, 400))
        self.frameActionsContent_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameActionsContent_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4.addWidget(self.frameActionsContent_2, 2, 0, 1, 1)

        self.stackedWidgetContent.addWidget(self.page)
        self.pageOperations = QWidget()
        self.pageOperations.setObjectName(u"pageOperations")
        self.gridLayout_17 = QGridLayout(self.pageOperations)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_21, 0, 0, 1, 1)

        self.frameOperationContainer = QFrame(self.pageOperations)
        self.frameOperationContainer.setObjectName(u"frameOperationContainer")
        self.frameOperationContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameOperationContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frameOperationContainer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frameOperationContent = QFrame(self.frameOperationContainer)
        self.frameOperationContent.setObjectName(u"frameOperationContent")
        self.frameOperationContent.setMinimumSize(QSize(300, 0))
        self.frameOperationContent.setMaximumSize(QSize(300, 16777215))
        self.frameOperationContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frameOperationContent.setFrameShadow(QFrame.Shadow.Plain)
        self.frameOperationContent.setLineWidth(0)
        self.frameOperationContent.setMidLineWidth(0)
        self.gridLayout_8 = QGridLayout(self.frameOperationContent)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDeleteData = QPushButton(self.frameOperationContent)
        self.pushButtonDeleteData.setObjectName(u"pushButtonDeleteData")
        self.pushButtonDeleteData.setMinimumSize(QSize(0, 46))
        self.pushButtonDeleteData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonDeleteData.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../icons/24x24/cil-trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonDeleteData.setIcon(icon6)
        self.pushButtonDeleteData.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButtonDeleteData, 1, 0, 1, 1)

        self.pushButtonCreateData = QPushButton(self.frameOperationContent)
        self.pushButtonCreateData.setObjectName(u"pushButtonCreateData")
        self.pushButtonCreateData.setMinimumSize(QSize(0, 46))
        self.pushButtonCreateData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonCreateData.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../icons/24x24/cil-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCreateData.setIcon(icon7)
        self.pushButtonCreateData.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButtonCreateData, 0, 0, 1, 1)

        self.pushButtonExportData = QPushButton(self.frameOperationContent)
        self.pushButtonExportData.setObjectName(u"pushButtonExportData")
        self.pushButtonExportData.setMinimumSize(QSize(0, 46))
        self.pushButtonExportData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonExportData.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../icons/24x24/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonExportData.setIcon(icon8)
        self.pushButtonExportData.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButtonExportData, 4, 0, 1, 1)

        self.pushButtonRefreshDashboard = QPushButton(self.frameOperationContent)
        self.pushButtonRefreshDashboard.setObjectName(u"pushButtonRefreshDashboard")
        self.pushButtonRefreshDashboard.setMinimumSize(QSize(0, 46))
        self.pushButtonRefreshDashboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonRefreshDashboard.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../icons/24x24/cil-chart-line.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonRefreshDashboard.setIcon(icon9)
        self.pushButtonRefreshDashboard.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButtonRefreshDashboard, 3, 0, 1, 1)

        self.pushButtonModifyData = QPushButton(self.frameOperationContent)
        self.pushButtonModifyData.setObjectName(u"pushButtonModifyData")
        self.pushButtonModifyData.setMinimumSize(QSize(0, 46))
        self.pushButtonModifyData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonModifyData.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"../icons/24x24/cil-pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonModifyData.setIcon(icon10)
        self.pushButtonModifyData.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButtonModifyData, 2, 0, 1, 1)

        self.treeWidgetExportedFiles = QTreeWidget(self.frameOperationContent)
        self.treeWidgetExportedFiles.setObjectName(u"treeWidgetExportedFiles")
        self.treeWidgetExportedFiles.header().setCascadingSectionResizes(False)
        self.treeWidgetExportedFiles.header().setHighlightSections(False)
        self.treeWidgetExportedFiles.header().setProperty("showSortIndicator", False)

        self.gridLayout_8.addWidget(self.treeWidgetExportedFiles, 5, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frameOperationContent, 0, 0, 1, 1)

        self.frameDataViewer = QFrame(self.frameOperationContainer)
        self.frameDataViewer.setObjectName(u"frameDataViewer")
        self.frameDataViewer.setMinimumSize(QSize(400, 0))
        self.frameDataViewer.setFrameShape(QFrame.Shape.NoFrame)
        self.frameDataViewer.setFrameShadow(QFrame.Shadow.Plain)
        self.frameDataViewer.setLineWidth(0)
        self.gridLayout_6 = QGridLayout(self.frameDataViewer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tableViewOperationData = QTableView(self.frameDataViewer)
        self.tableViewOperationData.setObjectName(u"tableViewOperationData")
        self.tableViewOperationData.setMinimumSize(QSize(0, 0))

        self.gridLayout_6.addWidget(self.tableViewOperationData, 1, 0, 1, 1)

        self.frameSearcher = QFrame(self.frameDataViewer)
        self.frameSearcher.setObjectName(u"frameSearcher")
        self.frameSearcher.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSearcher.setFrameShadow(QFrame.Shadow.Plain)
        self.frameSearcher.setLineWidth(0)
        self.gridLayout_7 = QGridLayout(self.frameSearcher)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEditSearcher = QLineEdit(self.frameSearcher)
        self.lineEditSearcher.setObjectName(u"lineEditSearcher")
        self.lineEditSearcher.setMinimumSize(QSize(0, 44))
        self.lineEditSearcher.setMaximumSize(QSize(16777215, 44))
        self.lineEditSearcher.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEditSearcher.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEditSearcher, 0, 0, 1, 1)

        self.pushButtonSearchData = QPushButton(self.frameSearcher)
        self.pushButtonSearchData.setObjectName(u"pushButtonSearchData")
        self.pushButtonSearchData.setMinimumSize(QSize(44, 44))
        self.pushButtonSearchData.setMaximumSize(QSize(44, 44))
        self.pushButtonSearchData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButtonSearchData.setStyleSheet(u"QPushButton {\n"
"	/* 0f69b4 | E0701E, D27B3C*/\n"
"	background-color:  #0f69b4;\n"
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
"	background-color: #121212;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../icons/24x24/cil-chevron-circle-right-alt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonSearchData.setIcon(icon11)
        self.pushButtonSearchData.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.pushButtonSearchData, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frameSearcher, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frameDataViewer, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.frameOperationContainer, 2, 0, 1, 1)

        self.stackedWidgetContent.addWidget(self.pageOperations)

        self.gridLayout_2.addWidget(self.stackedWidgetContent, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameContainer, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

        self.stackedWidgetContent.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonSwipeSidebar.setText("")
        self.pushButtonIndex.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.pushButtonProfile.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.pushButtonActions.setText(QCoreApplication.translate("MainWindow", u"Acciones", None))
        self.pushButtonOperations.setText(QCoreApplication.translate("MainWindow", u"Instituciones", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.labelIndexTitle_2.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.labelHome.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acciones", None))
        self.pushButtonDeleteData.setText(QCoreApplication.translate("MainWindow", u"Eliminar un registro", None))
        self.pushButtonCreateData.setText(QCoreApplication.translate("MainWindow", u"Crear un registro nuevo", None))
        self.pushButtonExportData.setText(QCoreApplication.translate("MainWindow", u"Exportar registros", None))
        self.pushButtonRefreshDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButtonModifyData.setText(QCoreApplication.translate("MainWindow", u"Modificar un registro", None))
        ___qtreewidgetitem = self.treeWidgetExportedFiles.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Archivos exportados", None));
        self.lineEditSearcher.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscador", None))
        self.pushButtonSearchData.setText("")
    # retranslateUi
