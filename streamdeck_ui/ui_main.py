# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 526)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.device_list = QComboBox(self.centralwidget)
        self.device_list.setObjectName(u"device_list")
        self.device_list.setMinimumSize(QSize(350, 0))

        self.horizontalLayout_4.addWidget(self.device_list)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 1))
        self.pushButton.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.pages = QTabWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"b")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_2 = QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pages.addTab(self.page_1, "")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pages.addTab(self.page_2, "")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_11 = QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pages.addTab(self.page_3, "")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_10 = QGridLayout(self.page_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pages.addTab(self.page_4, "")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_9 = QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pages.addTab(self.page_5, "")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_8 = QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pages.addTab(self.page_6, "")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_7 = QGridLayout(self.page_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pages.addTab(self.page_7, "")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_6 = QGridLayout(self.page_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pages.addTab(self.page_8, "")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_5 = QGridLayout(self.page_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pages.addTab(self.page_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_4 = QGridLayout(self.tab_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pages.addTab(self.tab_10, "")

        self.verticalLayout_6.addWidget(self.pages)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(40, -1, -1, -1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 20)
        self.text = QLineEdit(self.centralwidget)
        self.text.setObjectName(u"text")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.text, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.top = QRadioButton(self.centralwidget)
        self.top.setObjectName(u"top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.top)

        self.middle = QRadioButton(self.centralwidget)
        self.middle.setObjectName(u"middle")

        self.horizontalLayout_3.addWidget(self.middle)

        self.bottom = QRadioButton(self.centralwidget)
        self.bottom.setObjectName(u"bottom")
        sizePolicy1.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy1)
        self.bottom.setChecked(True)

        self.horizontalLayout_3.addWidget(self.bottom)


        self.gridLayout_12.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout_12)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.image = QToolButton(self.centralwidget)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(64, 64))
        self.image.setIconSize(QSize(64, 64))

        self.verticalLayout_7.addWidget(self.image)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.select_action = QComboBox(self.centralwidget)
        self.select_action.addItem("")
        self.select_action.setObjectName(u"select_action")

        self.verticalLayout_4.addWidget(self.select_action)

        self.plugin = QVBoxLayout()
        self.plugin.setSpacing(0)
        self.plugin.setObjectName(u"plugin")
        self.plugin.setContentsMargins(-1, 20, -1, 20)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.plugin.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_4.addLayout(self.plugin)

        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")

        self.verticalLayout_4.addWidget(self.add)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_4.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_actions = QLabel(self.centralwidget)
        self.label_actions.setObjectName(u"label_actions")

        self.horizontalLayout_5.addWidget(self.label_actions)

        self.horizontalSpacer_actions = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_actions)

        self.down = QToolButton(self.centralwidget)
        self.down.setObjectName(u"down")
        icon = QIcon()
        icon.addFile(u"../art/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.down.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.down)

        self.up = QToolButton(self.centralwidget)
        self.up.setObjectName(u"up")
        icon1 = QIcon()
        icon1.addFile(u"../art/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.up)

        self.remove = QToolButton(self.centralwidget)
        self.remove.setObjectName(u"remove")
        icon2 = QIcon()
        icon2.addFile(u"../art/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.remove)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1053, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stream Deck UI", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
        self.pages.setTabText(self.pages.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.pages.setTabText(self.pages.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"2", None))
        self.pages.setTabText(self.pages.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"3", None))
        self.pages.setTabText(self.pages.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"4", None))
        self.pages.setTabText(self.pages.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"5", None))
        self.pages.setTabText(self.pages.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"6", None))
        self.pages.setTabText(self.pages.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"7", None))
        self.pages.setTabText(self.pages.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"8", None))
        self.pages.setTabText(self.pages.indexOf(self.page_9), QCoreApplication.translate("MainWindow", u"9", None))
        self.pages.setTabText(self.pages.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"10", None))
        self.text.setInputMask("")
        self.text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Button text", None))
        self.top.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.middle.setText(QCoreApplication.translate("MainWindow", u"Middle", None))
        self.bottom.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.select_action.setItemText(0, QCoreApplication.translate("MainWindow", u"Select an action", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Select an **action** to perform from the list above, and configure the action here. Add it to the list of actions to perform, and you're all set!", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"Add to list  >", None))
        self.label_actions.setText(QCoreApplication.translate("MainWindow", u"Actions:", None))
        self.down.setText(QCoreApplication.translate("MainWindow", u"\u2b06\ufe0f", None))
        self.up.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.remove.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

