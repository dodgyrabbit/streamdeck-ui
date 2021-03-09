#!/bin/bash -xe

poetry run pyside2-uic streamdeck_ui/main.ui > streamdeck_ui/ui_main.py
poetry run pyside2-uic streamdeck_ui/preferences.ui > streamdeck_ui/ui_preferences.py
poetry run pyside2-uic streamdeck_ui/plugins/command/action_command.ui > streamdeck_ui/plugins/command/ui_action_command.py
poetry run pyside2-uic streamdeck_ui/plugins/text/action_text.ui > streamdeck_ui/plugins/text/ui_action_text.py
