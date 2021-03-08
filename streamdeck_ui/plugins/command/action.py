from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
from streamdeck_ui.plugins.command.ui_action_command import Ui_action_command
from PySide2.QtGui import QIcon


class Action:
    """
    asdfasdf
    """
    def __init__(self):
        print("Created an action")

    def get_name(self):
        return "Run command"

    def get_category(self):
        return "Keyboard"

    def get_icon(self) -> QIcon:
        return QIcon("streamdeck_ui/plugins/command/keyboard_24.png")

    def get_ui(self, parent, settings):
        return ActionCommand(parent)


class ActionCommand(QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        #super(Ui_action_command, self).__init__(parent)
        self.ui = Ui_action_command()
        self.ui.setupUi(self)
        self.show()
