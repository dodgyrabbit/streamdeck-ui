from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
from streamdeck_ui.plugins.text.ui_action_text import Ui_action_text
from PySide2.QtGui import QIcon
from streamdeck_ui.plugin import Plugin
import os


class Action(Plugin):
    def __init__(self):
        super().__init__("Type text", "Keyboard", __file__)

    def get_ui(self, parent, settings):
        return ActionText(parent)


class ActionText(QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        #super(Ui_action_command, self).__init__(parent)
        self.ui = Ui_action_text()
        self.ui.setupUi(self)
        self.show()
