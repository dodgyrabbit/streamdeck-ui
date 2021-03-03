"""Defines the QT powered interface for configuring Stream Decks"""
import os
import sys
import time
from functools import partial

from PySide2 import QtWidgets
from PySide2.QtCore import QSize, Qt, QTimer, QMimeData
from PySide2.QtGui import QIcon, QDrag
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QFileDialog,
    QMainWindow,
    QMenu,
    QSizePolicy,
    QSystemTrayIcon,
)

from streamdeck_ui import api
from streamdeck_ui.config import LOGO, PROJECT_PATH, STATE_FILE
from streamdeck_ui.ui_main import Ui_MainWindow

BUTTON_STYLE = """
    QToolButton{background-color:black; color:white;}
    QToolButton:checked{background-color:darkGray; color:black;}
    QToolButton:focus{border:none; }
"""

BUTTON_DRAG_STYLE = """
    QToolButton{background-color:white; color:black;}
    QToolButton:checked{background-color:darkGray; color:black;}
    QToolButton:focus{border:none; }
"""

selected_button: QtWidgets.QToolButton
text_timer = None


class DraggableButton(QtWidgets.QToolButton):
    """A QToolButton that supports drag and drop and swaps the button properties on drop """
    def __init__(self, parent, ui):
        super(DraggableButton, self).__init__(parent)

        self.setAcceptDrops(True)
        self.ui = ui

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.LeftButton:
            return

        mimedata = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimedata)
        drag.exec_(Qt.MoveAction)

    def dropEvent(self, e):
        global selected_button

        self.setStyleSheet(BUTTON_STYLE)

        # Ignore drag and drop on yourself
        if e.source().index == self.index:
            return

        api.swap_buttons(_deck_id(self.ui), _page(self.ui), e.source().index, self.index)
        # In the case that we've dragged the currently selected button, we have to
        # check the target button instead so it appears that it followed the drag/drop
        if e.source().isChecked():
            e.source().setChecked(False)
            self.setChecked(True)
            selected_button = self

        redraw_buttons(self.ui)

    def dragEnterEvent(self, e):
        if (type(self) is DraggableButton):
            e.setAccepted(True)
            self.setStyleSheet(BUTTON_DRAG_STYLE)
        else:
            e.setAccepted(False)

    def dragLeaveEvent(self, e):
        self.setStyleSheet(BUTTON_STYLE)


def _deck_id(ui) -> str:
    return ui.device_list.itemData(ui.device_list.currentIndex())


def _page(ui) -> int:
    return ui.pages.currentIndex()


def update_button_kasa_plug_ip(ui, text: str) -> None:
    deck_id = _deck_id(ui)
    api.set_button_kasa_plug_ip(deck_id, _page(ui), selected_button.index, text)
    redraw_buttons(ui)

def update_button_obs_password(ui, text: str) -> None:
    api.set_obs_password(text)


def update_button_obs_scene(ui, text: str) -> None:
    deck_id = _deck_id(ui)
    api.set_button_obs_scene(deck_id, _page(ui), selected_button.index, text)
    redraw_buttons(ui)


def update_button_text(ui, text: str) -> None:
    deck_id = _deck_id(ui)
    api.set_button_text(deck_id, _page(ui), selected_button.index, text)
    redraw_buttons(ui)


def update_button_command(ui, command: str) -> None:
    deck_id = _deck_id(ui)
    api.set_button_command(deck_id, _page(ui), selected_button.index, command)


def update_button_keys(ui, keys: str) -> None:
    deck_id = _deck_id(ui)
    api.set_button_keys(deck_id, _page(ui), selected_button.index, keys)


def update_button_write(ui) -> None:
    deck_id = _deck_id(ui)
    api.set_button_write(deck_id, _page(ui), selected_button.index, ui.write.toPlainText())


def update_change_brightness(ui, amount: int) -> None:
    deck_id = _deck_id(ui)
    api.set_button_change_brightness(deck_id, _page(ui), selected_button.index, amount)


def update_switch_page(ui, page: int) -> None:
    deck_id = _deck_id(ui)
    api.set_button_switch_page(deck_id, _page(ui), selected_button.index, page)


def _highlight_first_button(ui) -> None:
    button = ui.pages.currentWidget().findChildren(QtWidgets.QToolButton)[0]
    button.setChecked(False)
    button.click()


def change_page(ui, page: int) -> None:
    api.set_page(_deck_id(ui), page)
    redraw_buttons(ui)
    _highlight_first_button(ui)


def select_image(window) -> None:
    file_name = QFileDialog.getOpenFileName(
        window, "Open Image", os.path.expanduser("~"), "Image Files (*.png *.jpg *.bmp)"
    )[0]
    deck_id = _deck_id(window.ui)
    api.set_button_icon(deck_id, _page(window.ui), selected_button.index, file_name)
    redraw_buttons(window.ui)


def redraw_buttons(ui) -> None:
    deck_id = _deck_id(ui)
    current_tab = ui.pages.currentWidget()
    buttons = current_tab.findChildren(QtWidgets.QToolButton)
    for button in buttons:
        button.setText(api.get_button_text(deck_id, _page(ui), button.index))
        button.setIcon(QIcon(api.get_button_icon(deck_id, _page(ui), button.index)))


def set_brightness(ui, value: int) -> None:
    deck_id = _deck_id(ui)
    api.set_brightness(deck_id, value)


def button_clicked(ui, clicked_button, buttons) -> None:
    # Indicate we're updating a global variable, the currently selected button
    global selected_button

    # Update it to the button currently being clicked
    selected_button = clicked_button

    # Uncheck all other buttons (except the one we're clicking now)
    for button in buttons:
        if button == clicked_button:
            continue

        button.setChecked(False)

    deck_id = _deck_id(ui)
    button_id = selected_button.index
    ui.text.setText(api.get_button_text(deck_id, _page(ui), button_id))
    ui.command.setText(api.get_button_command(deck_id, _page(ui), button_id))
    ui.keys.setText(api.get_button_keys(deck_id, _page(ui), button_id))
    ui.write.setPlainText(api.get_button_write(deck_id, _page(ui), button_id))
    ui.change_brightness.setValue(api.get_button_change_brightness(deck_id, _page(ui), button_id))
    ui.switch_page.setValue(api.get_button_switch_page(deck_id, _page(ui), button_id))
    ui.obs_scene.setText(api.get_button_obs_scene(deck_id, _page(ui), button_id))
    ui.kasa_plug_ip.setText(api.get_button_kasa_plug_ip(deck_id, _page(ui), button_id))

def build_buttons(ui, tab) -> None:
    deck_id = _deck_id(ui)
    deck = api.get_deck(deck_id)

    if hasattr(tab, "deck_buttons"):
        tab.deck_buttons.hide()
        tab.deck_buttons.deleteLater()

    base_widget = QtWidgets.QWidget(tab)
    tab.children()[0].addWidget(base_widget)
    tab.deck_buttons = base_widget

    row_layout = QtWidgets.QVBoxLayout(base_widget)
    index = 0
    buttons = []
    for _row in range(deck["layout"][0]):  # type: ignore
        column_layout = QtWidgets.QHBoxLayout()
        row_layout.addLayout(column_layout)

        for _column in range(deck["layout"][1]):  # type: ignore
            button = DraggableButton(base_widget, ui)
            button.setCheckable(True)
            button.index = index
            button.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            button.setIconSize(QSize(100, 100))
            button.setStyleSheet(BUTTON_STYLE)
            buttons.append(button)
            column_layout.addWidget(button)
            index += 1

    # Note that the button click event captures the ui variable, the current button
    #  and all the other buttons
    for button in buttons:
        button.clicked.connect(
            lambda button=button, buttons=buttons: button_clicked(ui, button, buttons)
        )

    redraw_buttons(ui)
    tab.hide()
    tab.show()


def export_config(window) -> None:
    file_name = QFileDialog.getSaveFileName(
        window, "Export Config", os.path.expanduser("~/streamdeck_ui_export.json"), "JSON (*.json)"
    )[0]
    if not file_name:
        return

    api.export_config(file_name)


def import_config(window) -> None:
    file_name = QFileDialog.getOpenFileName(
        window, "Import Config", os.path.expanduser("~"), "Config Files (*.json)"
    )[0]
    if not file_name:
        return

    api.import_config(file_name)
    redraw_buttons(window.ui)


def sync(ui) -> None:
    api.ensure_decks_connected()
    ui.brightness.setValue(api.get_brightness(_deck_id(ui)))
    ui.pages.setCurrentIndex(api.get_page(_deck_id(ui)))


def build_device(ui, _device_index=None) -> None:
    for page_id in range(ui.pages.count()):
        page = ui.pages.widget(page_id)
        page.setStyleSheet("background-color: black")
        build_buttons(ui, page)

    sync(ui)
    _highlight_first_button(ui)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.window_shown: bool = True

    def closeEvent(self, event) -> None:  # noqa: N802 - Part of QT signature.
        self.window_shown = False
        self.hide()
        event.ignore()

    def systray_clicked(self, _status=None) -> None:
        self.hide()
        if self.window_shown:
            self.window_shown = False
            return

        self.show()
        self.activateWindow()
        getattr(self, "raise")()  # noqa: B009 - Can't call as self.raise() due to syntax error.
        self.window_shown = True


def queue_text_change(ui, text: str) -> None:
    global text_timer

    if text_timer:
        text_timer.stop()

    text_timer = QTimer()
    text_timer.setSingleShot(True)
    text_timer.timeout.connect(partial(update_button_text, ui, text))
    text_timer.start(500)


def start(_exit: bool = False) -> None:
    app = QApplication(sys.argv)

    first_start = False
    if not os.path.isfile(STATE_FILE):
        first_start = True

    logo = QIcon(LOGO)
    main_window = MainWindow()
    ui = main_window.ui
    main_window.setWindowIcon(logo)
    tray = QSystemTrayIcon(logo, app)
    tray.activated.connect(main_window.systray_clicked)

    menu = QMenu()
    action_config = QAction("Configure")
    action_config.triggered.connect(main_window.show)
    action_exit = QAction("Exit")
    action_exit.triggered.connect(app.exit)
    menu.addAction(action_config)
    menu.addAction(action_exit)

    tray.setContextMenu(menu)

    ui.kasa_plug_ip.textChanged.connect(partial(update_button_kasa_plug_ip, ui))
    ui.obs_password.textChanged.connect(partial(update_button_obs_password, ui))
    ui.obs_scene.textChanged.connect(partial(update_button_obs_scene, ui))
    ui.text.textChanged.connect(partial(queue_text_change, ui))
    ui.command.textChanged.connect(partial(update_button_command, ui))
    ui.keys.textChanged.connect(partial(update_button_keys, ui))
    ui.write.textChanged.connect(partial(update_button_write, ui))
    ui.change_brightness.valueChanged.connect(partial(update_change_brightness, ui))
    ui.switch_page.valueChanged.connect(partial(update_switch_page, ui))
    ui.imageButton.clicked.connect(partial(select_image, main_window))
    ui.brightness.valueChanged.connect(partial(set_brightness, ui))

    items = api.open_decks().items()
    print("wait for device(s)")

    while len(items) == 0:
        time.sleep(3)
        items = api.open_decks().items()

    print("found " + str(len(items)))

    for deck_id, deck in items:
        ui.device_list.addItem(f"{deck['type']} - {deck_id}", userData=deck_id)

    build_device(ui)
    ui.device_list.currentIndexChanged.connect(partial(build_device, ui))

    ui.pages.currentChanged.connect(partial(change_page, ui))

    ui.actionExport.triggered.connect(partial(export_config, main_window))
    ui.actionImport.triggered.connect(partial(import_config, main_window))
    ui.actionExit.triggered.connect(app.exit)

    timer = QTimer()
    timer.timeout.connect(partial(sync, ui))
    timer.start(1000)

    api.render()
    tray.show()
    if first_start:
        main_window.show()

    if _exit:
        return
    else:
        app.exec_()
        api.close_decks()
        sys.exit()


if __name__ == "__main__":
    start()
