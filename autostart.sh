#!/bin/bash

# Set keyboard layout to GB
setxkbmap gb
setxkbmap -option ""

# Set wallpaper from your collection (random selection)
feh --bg-fill --randomize "/home/linuxfinn/Documents/Wallpaper/Wallpaper/"* &

# Start services (only if not running)
if ! pgrep -x "picom" > /dev/null; then picom & fi
if ! pgrep -x "nm-applet" > /dev/null; then nm-applet & fi
if ! pgrep -x "dunst" > /dev/null; then dunst & fi
if ! pgrep -x "nextcloud" > /dev/null; then nextcloud & fi

sleep 1
