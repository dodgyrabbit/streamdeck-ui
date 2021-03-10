from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
from streamdeck_ui.plugins.command.ui_action_command import Ui_action_command
from streamdeck_ui.plugin import Plugin


class Action(Plugin):
    def __init__(self):
        super().__init__("Run command", "Keyboard", __file__)

    def get_ui(self, parent, settings):
        return ActionCommand(parent)


class ActionCommand(QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        #super(Ui_action_command, self).__init__(parent)
        self.ui = Ui_action_command()
        self.ui.setupUi(self)
        self.show()
