from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
from streamdeck_ui.plugins.text.ui_action_text import Ui_action_text
from PySide2.QtGui import QIcon


class Action:
    """
    asdfasdf
    """
    def __init__(self):
        print("Created an action")

    def get_name(self):
        return "Type text"

    def get_category(self):
        return "Keyboard"

    def get_icon(self) -> QIcon:
        return QIcon("streamdeck_ui/plugins/text/text_24.png")

    def get_ui(self, parent, settings):
        return ActionText(parent)


class ActionText(QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        #super(Ui_action_command, self).__init__(parent)
        self.ui = Ui_action_text()
        self.ui.setupUi(self)
        self.show()
