#!/bin/bash -xe

poetry run pyside2-uic streamdeck_ui/main.ui > streamdeck_ui/ui_main.py
poetry run pyside2-uic streamdeck_ui/preferences.ui > streamdeck_ui/ui_preferences.py
poetry run pyside2-uic streamdeck_ui/action_command.ui > streamdeck_ui/ui_action_command.py
