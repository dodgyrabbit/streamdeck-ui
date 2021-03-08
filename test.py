from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui, QtCore
import sys, os
from PySide2.QtWidgets import (
    QComboBox)

class CheckableComboBox(QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))
        self.

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

class Dialog_01(QMainWindow):
    def __init__(self):
        super(Dialog_01,self).__init__()
        myQWidget = QWidget()
        myBoxLayout = QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)
        
        self.ComboBox = CheckableComboBox()
        for i in range(3):
            self.ComboBox.addItem("Combobox Item " + str(i))
            item = self.ComboBox.model().item(i, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        
        self.toolbutton = QToolButton(self)
        self.toolbutton.setText('Select Categories ')
        
        self.toolmenu = QMenu(self)
        for i in range(3):
            action = self.toolmenu.addAction("Category " + str(i))
            action.setCheckable(True)
        
        self.toolbutton.set
        self.toolbutton.setMenu(self.toolmenu)
        self.toolbutton.setPopupMode(QToolButton.InstantPopup)
        myBoxLayout.addWidget(self.toolbutton)
        myBoxLayout.addWidget(self.ComboBox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog_1 = Dialog_01()
    dialog_1.show()
    dialog_1.resize(480,320)
    sys.exit(app.exec_())
