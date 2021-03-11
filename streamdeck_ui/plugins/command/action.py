from PySide2.QtWidgets import QWidget
from streamdeck_ui.plugins.command.ui_commandwidget import Ui_CommandWidget
from streamdeck_ui.plugin import Plugin


class Action(Plugin):
    def __init__(self):
        super().__init__("Run command", "Keyboard", __file__)

    def get_ui(self, parent, settings):
        return CommandWidget(parent)


class CommandWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CommandWidget()
        self.ui.setupUi(self)
        self.show()
