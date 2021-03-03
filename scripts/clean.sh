#!/bin/bash
set -euxo pipefail

poetry run isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 --recursive streamdeck_ui/ tests/ --exclude ui_main.py
poetry run black streamdeck_ui/ tests/ -l 100 --skip ui_main.py
