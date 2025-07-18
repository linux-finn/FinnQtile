# FinnQtile

My personal qtile configuration for Arch Linux.

## Features
- JetBrains Mono font
- Gruvbox-inspired color scheme
- Useful status bar widgets (CPU, RAM, network, volume, battery)
- Keybindings optimized for daily workflow
- Auto-wallpaper setup with feh

## Applications
- Terminal: alacritty
- Browser: qutebrowser
- File Manager: ranger
- Editor: neovim
- PDF Viewer: zathura
- Media Player: mpv

## Installation
1. Install qtile: `sudo pacman -S qtile`
2. Install dependencies: `sudo pacman -S alacritty feh picom ttf-jetbrains-mono`
3. Copy config.py to `~/.config/qtile/`
4. Copy autostart.sh to `~/.config/qtile/` and make executable
5. Set your wallpaper path in autostart.sh

## Key Bindings
- `Super + Enter` - Terminal
- `Super + b` - Browser
- `Super + e` - File manager
- `Super + d` - App launcher
- `Super + w` - Close window
- `Super + 1-9` - Switch workspaces
