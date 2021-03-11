#!/bin/bash -xe

poetry run pyside2-uic streamdeck_ui/main.ui > streamdeck_ui/ui_main.py
poetry run pyside2-uic streamdeck_ui/preferences.ui > streamdeck_ui/ui_preferences.py
poetry run pyside2-uic streamdeck_ui/plugins/command/commandwidget.ui > streamdeck_ui/plugins/command/ui_commandwidget.py
poetry run pyside2-uic streamdeck_ui/plugins/text/text.ui > streamdeck_ui/plugins/text/ui_text.py
