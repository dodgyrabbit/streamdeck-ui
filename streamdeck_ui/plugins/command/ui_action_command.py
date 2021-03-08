# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'action_command.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_action_command(object):
    def setupUi(self, action_command):
        if not action_command.objectName():
            action_command.setObjectName(u"action_command")
        action_command.resize(414, 287)
        self.verticalLayout = QVBoxLayout(action_command)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.label = QLabel(action_command)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.command = QLineEdit(action_command)
        self.command.setObjectName(u"command")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.command)

        self.label_2 = QLabel(action_command)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.label_2)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(action_command)

        QMetaObject.connectSlotsByName(action_command)
    # setupUi

    def retranslateUi(self, action_command):
        action_command.setWindowTitle(QCoreApplication.translate("action_command", u"Form", None))
        self.label.setText(QCoreApplication.translate("action_command", u"Command:", None))
        self.label_2.setText(QCoreApplication.translate("action_command", u"Use the **command** action to run a program on your computer. For example, type **code** to launch Visual Studio Code (assuming you have it installed of course!)", None))
    # retranslateUi

