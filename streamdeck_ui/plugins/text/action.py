from PySide2.QtWidgets import QWidget
from streamdeck_ui.plugins.text.ui_text import Ui_text
from streamdeck_ui.plugin import Plugin


class Action(Plugin):
    def __init__(self):
        super().__init__("Type text", "Keyboard", __file__)

    def get_ui(self, parent, settings):
        return TextWidget(parent)


class TextWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_text()
        self.ui.setupUi(self)
        self.show()
