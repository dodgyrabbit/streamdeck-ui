[![streamdeck_ui - Linux compatible UI for the Elgato Stream Deck](art/logo_large.png)](https://timothycrosley.github.io/streamdeck-ui/)
_________________

[![PyPI version](https://badge.fury.io/py/streamdeck-ui.svg)](http://badge.fury.io/py/streamdeck-ui)
[![Build Status](https://travis-ci.org/timothycrosley/streamdeck-ui.svg?branch=master)](https://travis-ci.org/timothycrosley/streamdeck-ui)
[![codecov](https://codecov.io/gh/timothycrosley/streamdeck-ui/branch/master/graph/badge.svg)](https://codecov.io/gh/timothycrosley/streamdeck-ui)
[![Join the chat at https://gitter.im/timothycrosley/streamdeck-ui](https://badges.gitter.im/timothycrosley/streamdeck-ui.svg)](https://gitter.im/timothycrosley/streamdeck-ui?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/streamdeck-ui/)
[![Downloads](https://pepy.tech/badge/streamdeck-ui)](https://pepy.tech/project/streamdeck-ui)
_________________

[Read Latest Documentation](https://timothycrosley.github.io/streamdeck-ui/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/streamdeck-ui/)
_________________

**streamdeck_ui** A Linux compatible UI for the Elgato Stream Deck.

## What is this?

The Streamdeck UI project is awesome but there are many pull requests and issues mentioned in the main repo. This is a fork where I can merge some of those PRs and get the app to be a bit more up to date.

### Change Log (compared to offical build)

#### 1. [Improved command handling](https://github.com/timothycrosley/streamdeck-ui/pull/20)
Commands with spaces were not handled properly. With this patch, the following command works properly:
```
xdotool search --name '^Meet - .+$' windowactivate --sync key ctrl+d
```
This script toggles the mute shortcut for Google Meet. Note that the meeting tab be active. You can still have multiple browser windows. If you have multiple screens with lots of tabs, I recommend just putting your meeting in it's own tab/window then this shortcut will always find it.

#### 2. Window title changed to Stream Deck UI

#### 3. Catch exception for invalid command
An invalid command with make Streamdeck UI hang. This change catches the exception and logs a warning.

#### 4. "Configure" menu item added to notification area
In addition to just double clicking, you have a menu item called Configure that shows the main config window.

#### 5. [Wait until device is plugged in](https://github.com/exmatrikulator/streamdeck-ui/commit/326109d9a2815a3f5507a7844122647780ac7a43)
This avoids the crash on startup if your Stream Deck is not plugged in.

#### 6. [Show configuration winow only the first time](https://github.com/exmatrikulator/streamdeck-ui/commit/ba25da606c9644a8b67d904ed28a0dfff0cf753a)
When you run streamdeck and you have already configured it, it will not show the config window. Access it via the notification area menu.

#### 7. [Show button text as white on black background](https://github.com/timothycrosley/streamdeck-ui/pull/91/files)
Previously it was black on black and you could not see the text until you put focus on a button.

#### 8. Change OBS Scene
Switch between OBS scenes. Password is supported, but not saved to settings file.
Install the [obs-websocket](https://github.com/Palakis/obs-websocket) plugin in OBS and select the scene you want to switch to when a button is pressed.

#### 9. Support for kasa smart plugs
Toggle your lights on/off.

#### 10. Drag and drop to rearrange your keys
![Drag and drop example](art/drag-drop.gif)

#### 11. Graceful shutdown
Fixes the following error on exit:
```
double free or corruption (fasttop)
Aborted (core dumped)
```

![Streamdeck UI Usage Example](art/example.gif)

## Key Features

* **Linux Compatible**: Enables usage of all Stream Deck devices on Linux without needing to code.
* **Multi-device**: Enables connecting and configuring multiple Stream Deck devices on one computer.
* **Brightness Control**: Supports controlling the brightness from both the configuration UI and buttons on the device itself.
* **Configurable Button Display**: Icons + Text, Icon Only, and Text Only configurable per button on the Stream Deck.
* **Multi-Action Support**: Run commands, write text and press hotkey combinations at the press of a single button on your Stream Deck.
* **Button Pages**: streamdeck_ui supports multiple pages of buttons and dynamically setting up buttons to switch between those pages.
* **Auto Reconnect**: Automatically and gracefully reconnects, in the case the device is unplugged and replugged in.
* **Import/Export**: Supports saving and restoring Stream Deck configuration.

Communication with the Streamdeck is powered by the [Python Elgato Stream Deck Library](https://github.com/abcminiuser/python-elgato-streamdeck#python-elgato-stream-deck-library).

## Linux Quick Start
### Precooked Scripts
There are scripts for setting up streamdeck_ui on [Debian/Ubuntu](scripts/ubuntu_install.sh) and [Fedora](scripts/fedora_install.sh).
### Manual installation
To use streamdeck_ui on Linux, you will need first to install some pre-requisite system libraries.
The name of those libraries will differ depending on your Operating System.  
Debian / Ubuntu:
```bash
sudo apt install libhidapi-hidraw0 libudev-dev libusb-1.0-0-dev python3-pip
```
Fedora:
```bash
sudo dnf install python3-devel libusb-devel python3-pip libusbx-devel libudev-devel
```
If you're using GNOME shell, you might need to manually install an extension that adds [KStatusNotifierItem/AppIndicator Support](https://extensions.gnome.org/extension/615/appindicator-support/) to make the tray icon show up.

To use streamdeck_ui without root permissions, you have to give your user full access to the device.

Add your user to the 'plugdev' group:
```bash
sudo usermod -a -G plugdev `whoami`
```
Add the udev rules using your text editor:
```bash
sudoedit /etc/udev/rules.d/99-streamdeck.rules
# If that doesn't work, try:
sudo nano /etc/udev/rules.d/99-streamdeck.rules
```
Paste the following lines:
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0060", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0063", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006c", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006d", MODE:="660", GROUP="plugdev"
```
Reload the rules:
```
sudo udevadm control --reload-rules
```
Make sure you unplug and replug your device before continuing.
Once complete, you should be able to install streamdeck_ui.
Installing the application itself is done via pip:
```bash
pip3 install --user streamdeck_ui
```
Make sure to include `$HOME/.local/bin` to your PATH.  
If you haven't already, add
```bash
PATH=$PATH:$HOME/.local/bin
```
to the bottom your shell config file (most likely .bashrc in your home directory)

You can then launch `streamdeck` to start configuring your device.

```bash
streamdeck
```

It's recommended that you include `streamdeck` in your windowing environment's list of applications to auto-start.

## Generic Quick Start

On other Operating Systems, you'll need to install the required [dependencies](https://github.com/abcminiuser/python-elgato-streamdeck#package-dependencies) of the library.
After that, use pip to install the app:

```bash
pip3 install streamdeck_ui --user
streamdeck
```
