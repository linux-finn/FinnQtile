#!/bin/bash

# Set wallpaper
feh --bg-fill '/home/linuxfinn/Downloads/Arch Wallpaper.png' &

# Start compositor for transparency and effects
picom &

# Start network manager applet
nm-applet &

# Start volume control applet
volumeicon &
setxkbmap -option altwin:swap_alt_win &
