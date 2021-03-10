# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'action_text.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_action_text(object):
    def setupUi(self, action_text):
        if not action_text.objectName():
            action_text.setObjectName(u"action_text")
        action_text.resize(414, 287)
        self.verticalLayout = QVBoxLayout(action_text)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(action_text)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.textEdit = QTextEdit(action_text)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.label_2 = QLabel(action_text)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(action_text)

        QMetaObject.connectSlotsByName(action_text)
    # setupUi

    def retranslateUi(self, action_text):
        action_text.setWindowTitle(QCoreApplication.translate("action_text", u"Form", None))
        self.label.setText(QCoreApplication.translate("action_text", u"Text:", None))
        self.label_2.setText(QCoreApplication.translate("action_text", u"Use the **text** action to type the text provided. It will simulate the keyboard typing the text, so you can use it in any program. For example, a common Email or document template.", None))
    # retranslateUi

