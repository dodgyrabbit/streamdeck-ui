# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(392, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(6)
        self.label_brightness = QLabel(Dialog)
        self.label_brightness.setObjectName(u"label_brightness")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_brightness)

        self.brightness = QSlider(Dialog)
        self.brightness.setObjectName(u"brightness")
        self.brightness.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.brightness)

        self.label_dim = QLabel(Dialog)
        self.label_dim.setObjectName(u"label_dim")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_dim)

        self.dim = QComboBox(Dialog)
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.addItem("")
        self.dim.setObjectName(u"dim")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dim)

        self.label_hide = QLabel(Dialog)
        self.label_hide.setObjectName(u"label_hide")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_hide)

        self.hide = QCheckBox(Dialog)
        self.hide.setObjectName(u"hide")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.hide)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_brightness.setText(QCoreApplication.translate("Dialog", u"Brightness:", None))
        self.label_dim.setText(QCoreApplication.translate("Dialog", u"Auto dim after:", None))
        self.dim.setItemText(0, QCoreApplication.translate("Dialog", u"Disabled", None))
        self.dim.setItemText(1, QCoreApplication.translate("Dialog", u"1 minute", None))
        self.dim.setItemText(2, QCoreApplication.translate("Dialog", u"2 minutes", None))
        self.dim.setItemText(3, QCoreApplication.translate("Dialog", u"3 minutes", None))
        self.dim.setItemText(4, QCoreApplication.translate("Dialog", u"4 minutes", None))
        self.dim.setItemText(5, QCoreApplication.translate("Dialog", u"5 minutes", None))
        self.dim.setItemText(6, QCoreApplication.translate("Dialog", u"10 minutes", None))
        self.dim.setItemText(7, QCoreApplication.translate("Dialog", u"15 minutes", None))
        self.dim.setItemText(8, QCoreApplication.translate("Dialog", u"30 minutes", None))
        self.dim.setItemText(9, QCoreApplication.translate("Dialog", u"1 hour", None))

        self.dim.setCurrentText(QCoreApplication.translate("Dialog", u"Disabled", None))
        self.label_hide.setText("")
        self.hide.setText(QCoreApplication.translate("Dialog", u"Hide on startup", None))
    # retranslateUi

