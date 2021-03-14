"""Defines the Python API for interacting with the StreamDeck Configuration UI"""
import json
import os
from functools import partial
import shlex
from subprocess import Popen  # nosec - Need to allow users to specify arbitrary commands
from typing import Dict, Tuple, Union
from warnings import warn

from PIL import Image, ImageDraw, ImageFont
from pynput.keyboard import Controller, Key
from StreamDeck import DeviceManager, ImageHelpers
from StreamDeck.Devices import StreamDeck
from StreamDeck.ImageHelpers import PILHelper
from streamdeck_ui.config import CONFIG_FILE_VERSION, DEFAULT_FONT, FONTS_PATH, STATE_FILE

from obswebsocket import obsws, requests

import asyncio
from kasa import SmartPlug

from PIL.ImageQt import ImageQt
from PySide2.QtGui import QPixmap, QImage

image_cache: Dict[str, Tuple[object, object]] = {}

decks: Dict[str, StreamDeck.StreamDeck] = {}
state: Dict[str, Dict[str, Union[int, Dict[int, Dict[int, Dict[str, str]]]]]] = {}

# The OBS password is not stored in the state dictionary. You have to set it up when running streamdeck.
# If it was stored with state, it would be in plain text. In future this could be improved.
obs_password = ""


def _key_change_callback(deck_id: str, _deck: StreamDeck.StreamDeck, key: int, state: bool) -> None:
    if state:
        keyboard = Controller()
        page = get_page(deck_id)

        command = get_button_command(deck_id, page, key)
        if command:
            try:
                Popen(shlex.split(command))
            except Exception as ex:
                warn(f"An error occurred when trying to execute the command {command}.\n\n{str(ex)}")
                pass

        keys = get_button_keys(deck_id, page, key)
        if keys:
            keys = keys.strip().replace(" ", "")
            for section in keys.split(","):
                for key_name in section.split("+"):
                    keyboard.press(getattr(Key, key_name.lower(), key_name))
                for key_name in section.split("+"):
                    keyboard.release(getattr(Key, key_name.lower(), key_name))

        write = get_button_write(deck_id, page, key)
        if write:
            keyboard.type(write)

        brightness_change = get_button_change_brightness(deck_id, page, key)
        if brightness_change:
            change_brightness(deck_id, brightness_change)

        switch_page = get_button_switch_page(deck_id, page, key)
        if switch_page:
            set_page(deck_id, switch_page - 1)

        obs_scene = get_button_obs_scene(deck_id, page, key)
        if obs_scene:
            host = "localhost"
            port = 4444

            try:
                ws = obsws(host, port, obs_password)
                ws.connect()
                ws.call(requests.SetCurrentScene(obs_scene))
                ws.disconnect()
            except Exception as error:
                warn(f"Error while trying to connect to OBS: {error}")
                pass

        kasa_plug_ip = get_button_kasa_plug_ip(deck_id, page, key)
        if kasa_plug_ip:
            try:
                p = SmartPlug(kasa_plug_ip)
                asyncio.run(p.update())
                if p.is_on:
                    asyncio.run(p.turn_off())
                else:
                    asyncio.run(p.turn_on())

            except Exception as error:
                warn(f"A {error} error occurred when trying to toggle plug {kasa_plug_ip}")
            pass


def _save_state():
    export_config(STATE_FILE)


def _open_config(config_file: str):
    global state

    with open(config_file) as state_file:
        config = json.loads(state_file.read())
        file_version = config.get("streamdeck_ui_version", 0)
        if file_version != CONFIG_FILE_VERSION:
            raise ValueError(
                "Incompatible version of config file found: "
                f"{file_version} does not match required version "
                f"{CONFIG_FILE_VERSION}."
            )

        state = {}
        for deck_id, deck in config["state"].items():
            deck["buttons"] = {
                int(page_id): {int(button_id): button for button_id, button in buttons.items()}
                for page_id, buttons in deck.get("buttons", {}).items()
            }
            state[deck_id] = deck


def import_config(config_file: str) -> None:
    _open_config(config_file)
    render()
    _save_state()


def export_config(output_file: str) -> None:
    with open(output_file, "w") as state_file:
        state_file.write(
            json.dumps(
                {"streamdeck_ui_version": CONFIG_FILE_VERSION, "state": state},
                indent=4,
                separators=(",", ": "),
            )
        )


def open_decks() -> Dict[str, Dict[str, Union[str, Tuple[int, int]]]]:
    """Opens and then returns all known stream deck devices"""
    for deck in DeviceManager.DeviceManager().enumerate():
        deck.open()
        deck.reset()
        deck_id = deck.get_serial_number()
        decks[deck_id] = deck
        deck.set_key_callback(partial(_key_change_callback, deck_id))

    return {
        deck_id: {"type": deck.deck_type(), "layout": deck.key_layout()}
        for deck_id, deck in decks.items()
    }


def close_decks() -> None:
    """Closes open decks for input/ouput."""
    for _deck_serial, deck in decks.items():
        if deck.connected():
            deck.close()


def ensure_decks_connected() -> None:
    """Reconnects to any decks that lost connection. If they did, re-renders them."""
    for deck_serial, deck in decks.copy().items():
        if not deck.connected():
            for new_deck in DeviceManager.DeviceManager().enumerate():
                try:
                    new_deck.open()
                    new_deck_serial = new_deck.get_serial_number()
                except Exception as error:
                    warn(f"A {error} error occurred when trying to reconnect to {deck_serial}")
                    new_deck_serial = None

                if new_deck_serial == deck_serial:
                    deck.close()
                    new_deck.reset()
                    new_deck.set_key_callback(partial(_key_change_callback, new_deck_serial))
                    decks[new_deck_serial] = new_deck
                    render()


def set_obs_password(password: str) -> None:
    global obs_password
    obs_password = password


def get_deck(deck_id: str) -> Dict[str, Dict[str, Union[str, Tuple[int, int]]]]:
    return {"type": decks[deck_id].deck_type(), "layout": decks[deck_id].key_layout()}


def _button_state(deck_id: str, page: int, button: int) -> dict:
    buttons = state.setdefault(deck_id, {}).setdefault("buttons", {})
    buttons_state = buttons.setdefault(page, {})  # type: ignore
    return buttons_state.setdefault(button, {})  # type: ignore


def swap_buttons(deck_id: str, page: int, source_button: int, target_button: int) -> None:
    """Swaps the properties of the source and target buttons"""
    temp = state[deck_id]["buttons"][page][source_button]
    state[deck_id]["buttons"][page][source_button] = state[deck_id]["buttons"][page][target_button]
    state[deck_id]["buttons"][page][target_button] = temp

    # Clear the cache so images will be recreated on render
    image_cache.pop(f"{deck_id}.{page}.{source_button}", None)
    image_cache.pop(f"{deck_id}.{page}.{target_button}", None)

    _save_state()
    render()


def set_button_text(deck_id: str, page: int, button: int, text: str) -> None:
    """Set the text associated with a button"""
    _button_state(deck_id, page, button)["text"] = text
    image_cache.pop(f"{deck_id}.{page}.{button}", None)
    render()
    _save_state()


def get_button_text(deck_id: str, page: int, button: int) -> str:
    """Returns the text set for the specified button"""
    return _button_state(deck_id, page, button).get("text", "")


def set_button_icon(deck_id: str, page: int, button: int, icon: str) -> None:
    """Sets the icon associated with a button"""
    _button_state(deck_id, page, button)["icon"] = icon
    image_cache.pop(f"{deck_id}.{page}.{button}", None)
    render()
    _save_state()


# FIXME: A number of issues to deal with here
# A get method should not have side effects
# Create secondary cache or move into different
# module to deal with QImage
# def get_button_icon(deck_id: str, page: int, button: int) -> str:
#    """Returns the icon set for a particular button"""
#    return _button_state(deck_id, page, button).get("icon", "")

def get_button_icon(deck_id: str, page: int, button: int) -> str:
    """Returns the icon set for a particular button"""
    key = f"{deck_id}.{page}.{button}"
    if key not in image_cache:
        print("Didn't find it in cache")
        render()
    return image_cache[key][1]


def set_button_change_brightness(deck_id: str, page: int, button: int, amount: int) -> None:
    """Sets the brightness changing associated with a button"""
    _button_state(deck_id, page, button)["brightness_change"] = amount
    render()
    _save_state()


def get_button_change_brightness(deck_id: str, page: int, button: int) -> int:
    """Returns the brightness change set for a particular button"""
    return _button_state(deck_id, page, button).get("brightness_change", 0)


def set_button_command(deck_id: str, page: int, button: int, command: str) -> None:
    """Sets the command associated with the button"""
    _button_state(deck_id, page, button)["command"] = command
    _save_state()


def get_button_command(deck_id: str, page: int, button: int) -> str:
    """Returns the command set for the specified button"""
    return _button_state(deck_id, page, button).get("command", "")


def set_button_switch_page(deck_id: str, page: int, button: int, switch_page: int) -> None:
    """Sets the page switch associated with the button"""
    _button_state(deck_id, page, button)["switch_page"] = switch_page
    _save_state()


def get_button_switch_page(deck_id: str, page: int, button: int) -> int:
    """Returns the page switch set for the specified button. 0 implies no page switch."""
    return _button_state(deck_id, page, button).get("switch_page", 0)


def set_button_keys(deck_id: str, page: int, button: int, keys: str) -> None:
    """Sets the keys associated with the button"""
    _button_state(deck_id, page, button)["keys"] = keys
    _save_state()


def get_button_keys(deck_id: str, page: int, button: int) -> str:
    """Returns the keys set for the specified button"""
    return _button_state(deck_id, page, button).get("keys", "")


def set_button_write(deck_id: str, page: int, button: int, write: str) -> None:
    """Sets the text meant to be written when button is pressed"""
    _button_state(deck_id, page, button)["write"] = write
    _save_state()


def get_button_write(deck_id: str, page: int, button: int) -> str:
    """Returns the text to be produced when the specified button is pressed"""
    return _button_state(deck_id, page, button).get("write", "")


def get_button_obs_scene(deck_id: str, page: int, button: int) -> str:
    """Returns the obs scene name when the specified button is pressed"""
    return _button_state(deck_id, page, button).get("obs_scene", "")


def set_button_obs_scene(deck_id: str, page: int, button: int, obs_scene: str) -> None:
    """Sets the obs scene name to switch to when button is pressed"""
    _button_state(deck_id, page, button)["obs_scene"] = obs_scene
    _save_state()


def get_button_kasa_plug_ip(deck_id: str, page: int, button: int) -> str:
    """Returns the IP address of the kasa plug"""
    return _button_state(deck_id, page, button).get("kasa_plug_ip", "")


def set_button_kasa_plug_ip(deck_id: str, page: int, button: int, kasa_plug_ip: str) -> None:
    """Sets the IP address of the kasa plug"""
    _button_state(deck_id, page, button)["kasa_plug_ip"] = kasa_plug_ip
    _save_state()


def set_brightness(deck_id: str, brightness: int) -> None:
    """Sets the brightness for every button on the deck"""
    decks[deck_id].set_brightness(brightness)
    state.setdefault(deck_id, {})["brightness"] = brightness
    _save_state()


def get_brightness(deck_id: str) -> int:
    """Gets the brightness that is set for the specified stream deck"""
    return state.get(deck_id, {}).get("brightness", 100)  # type: ignore


def change_brightness(deck_id: str, amount: int = 1) -> None:
    """Change the brightness of the deck by the specified amount"""
    set_brightness(deck_id, max(min(get_brightness(deck_id) + amount, 100), 0))


def get_page(deck_id: str) -> int:
    """Gets the current page shown on the stream deck"""
    return state.get(deck_id, {}).get("page", 0)  # type: ignore


def set_page(deck_id: str, page: int) -> None:
    """Sets the current page shown on the stream deck"""
    state.setdefault(deck_id, {})["page"] = page
    render()
    _save_state()


def render() -> None:
    """renders all decks"""
    for deck_id, deck_state in state.items():
        deck = decks.get(deck_id, None)
        if not deck:
            warn(f"{deck_id} has settings specified but is not seen. Likely unplugged!")
            continue

        page = get_page(deck_id)
        for button_id, button_settings in (
            deck_state.get("buttons", {}).get(page, {}).items()  # type: ignore
        ):
            key = f"{deck_id}.{page}.{button_id}"
            if key in image_cache:
                image = image_cache[key][0]
            else:
                pil_image = _render_key_image(deck, **button_settings)
                image = ImageHelpers.PILHelper.to_native_format(deck, pil_image)

                qt_image = ImageQt(pil_image)
                qt_image = qt_image.convertToFormat(QImage.Format_ARGB32)
                pixmap = QPixmap(qt_image)

                image_cache[key] = (image, pixmap)

            deck.set_key_image(button_id, image)


def _render_key_image(deck, icon: str = "", text: str = "", font: str = DEFAULT_FONT, **kwargs):
    """Renders an individual key image and returns
    it as a PIL image"""
    image = PILHelper.create_image(deck)
    draw = ImageDraw.Draw(image)

    if icon:
        rgba_icon = Image.open(icon).convert("RGBA")
    else:
        rgba_icon = Image.new("RGBA", (300, 300))

    icon_width, icon_height = image.width, image.height
    if text:
        icon_height -= 20

    rgba_icon.thumbnail((icon_width, icon_height), Image.LANCZOS)
    icon_pos = ((image.width - rgba_icon.width) // 2, 0)
    image.paste(rgba_icon, icon_pos, rgba_icon)

    if text:
        true_font = ImageFont.truetype(os.path.join(FONTS_PATH, font), 14)
        label_w, label_h = draw.textsize(text, font=true_font)
        if icon:
            label_pos = ((image.width - label_w) // 2, image.height - 20)
        else:
            label_pos = ((image.width - label_w) // 2, (image.height // 2) - 7)
        draw.text(label_pos, text=text, font=true_font, fill="white")

    return image


if os.path.isfile(STATE_FILE):
    _open_config(STATE_FILE)
