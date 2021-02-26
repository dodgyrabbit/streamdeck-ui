#!/bin/bash -xe

poetry run pyside6-uic streamdeck_ui/main.ui > streamdeck_ui/ui_main.py
