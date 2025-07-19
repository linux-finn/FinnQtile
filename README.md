```markdown
# FinnQtile

My personal qtile tiling window manager configuration for Arch Linux. A clean, functional setup optimized for productivity and daily workflow with Alt-based keybindings.

## Screenshots
*Screenshots of the actual setup coming soon*

## Features

### Visual Design
- **Font**: JetBrains Mono (size 14)
- **Color Scheme**: Gruvbox-inspired theme with warm, easy-on-the-eyes colors
- **Status Bar**: Comprehensive system monitoring with all essential widgets
- **Layouts**: Multiple tiling layouts for different workflow needs
- **Wallpapers**: Random wallpaper selection from personal collection

### Status Bar Widgets
- **Current Layout** - Shows active window layout
- **Workspaces** - Clean numbered workspaces (1-9)
- **Window Name** - Current focused window title
- **CPU Usage** - Real-time processor load percentage
- **Memory Usage** - Current RAM consumption in MB
- **Network** - Upload/download speeds with proper formatting
- **Volume** - Current audio volume level
- **Power** - AC Power indicator for desktop, battery info for laptops
- **System Tray** - System notification icons (includes WiFi management)
- **Clock** - UK format date/time (DD/MM/YYYY, 12-hour AM/PM)
- **Power Button** - Quick exit with confirmation

### Application Integration
- **Terminal**: alacritty
- **Browser**: qutebrowser
- **File Manager**: ranger (terminal-based) + thunar (GUI)
- **Editor**: neovim
- **PDF Viewer**: zathura
- **Media Player**: mpv
- **App Launcher**: rofi
- **Notifications**: dunst
- **Compositor**: picom
- **WiFi Management**: nm-applet (system tray)

### Window Layouts
- **Columns**: Side-by-side tiling (default)
- **Max**: Single window fullscreen
- **MonadTall**: Main window + side stack
- **Floating**: Traditional overlapping windows

## Installation

### Prerequisites
```bash
# Install qtile and core dependencies
sudo pacman -S qtile alacritty python-psutil

# Install applications
sudo pacman -S qutebrowser ranger neovim zathura mpv rofi

# Install utilities and system components
sudo pacman -S feh flameshot picom dunst nm-applet pavucontrol
sudo pacman -S ttf-jetbrains-mono noto-fonts-emoji

# Install optional packages
sudo pacman -S thunar firefox thunderbird discord gimp obs-studio
```

### Clone and Install
```bash
# Clone this repository
git clone https://github.com/linux-finn/FinnQtile.git
cd FinnQtile

# Create qtile config directory
mkdir -p ~/.config/qtile

# Copy configuration files
cp config.py ~/.config/qtile/
cp autostart.sh ~/.config/qtile/
chmod +x ~/.config/qtile/autostart.sh
```

### Wallpaper Setup
```bash
# Create wallpaper directory (or use your existing one)
mkdir -p ~/Documents/Wallpaper/Wallpaper/

# Add your wallpapers to this directory
# The config will randomly select one on startup
```

### Test Configuration
```bash
# Test the configuration syntax
python -m py_compile ~/.config/qtile/config.py

# If no errors, log into qtile from your display manager
```

## Keybindings

**Note**: This configuration uses **Alt** as the mod key (not Super/Windows key) due to hardware compatibility.

### Core Window Management
| Keybinding | Action |
|---|---|
| Alt + Return | Open terminal (alacritty) |
| Alt + d | Launch rofi application launcher |
| Alt + w | Close window |
| Alt + f | Toggle fullscreen |
| Alt + t | Toggle floating mode |

### Application Launchers
| Keybinding | Application |
|---|---|
| Alt + b | qutebrowser |
| Alt + e | ranger (file manager) |
| Alt + v | neovim |
| Alt + m | mpv |
| Alt + z | zathura (PDF viewer) |
| Alt + s | Screenshot (flameshot) |

### Window Navigation
| Keybinding | Action |
|---|---|
| Alt + h/j/k/l | Move focus left/down/up/right |
| Alt + Shift + h/j/k/l | Move window left/down/up/right |
| Alt + Ctrl + h/j/k/l | Resize window |
| Alt + n | Reset window sizes |
| Alt + Space | Move to next window |

### Layout and Workspace Management
| Keybinding | Action |
|---|---|
| Alt + Tab | Switch between layouts |
| Alt + 1-9 | Switch to workspace 1-9 |
| Alt + Shift + 1-9 | Move window to workspace 1-9 |

### System Controls
| Keybinding | Action |
|---|---|
| Alt + Ctrl + r | Reload qtile configuration |
| Alt + Ctrl + q | Quit qtile |
| Alt + r | Qtile command prompt |
| Alt + Shift + w | Change wallpaper (random) |

## Configuration

### Customizing Colors
Edit the `colors` dictionary in `config.py`:
```python
colors = {
    'bg': '#282828',        # Background
    'fg': '#ebdbb2',        # Foreground
    'blue': '#458588',      # Accent color
    'green': '#98971a',     # Success/CPU
    'yellow': '#d79921',    # Warning/Memory
    'red': '#cc241d',       # Error/Critical
    'purple': '#b16286',    # Network
    'orange': '#d65d0e',    # Volume
    'aqua': '#689d6a',      # Power
    'gray': '#a89984'       # Separators
}
```

### Adding Applications to Autostart
Edit `autostart.sh` to launch applications at startup:
```bash
# Add after the existing services
discord &
spotify &
your-app &
```

### Changing Wallpaper Directory
Update the wallpaper path in `autostart.sh`:
```bash
# Change this line:
feh --bg-fill --randomize "/home/yourusername/path/to/wallpapers/"* &
```

## Hardware Compatibility

### Mod Key Configuration
This configuration uses Alt (mod1) as the mod key instead of Super (mod4) due to hardware-level key mapping issues on some systems. If your hardware works correctly with the Super key, you can change this in `config.py`:

```python
# Change from:
mod = "mod1"  # Alt key
# To:
mod = "mod4"  # Super/Windows key
```

### WiFi Management
WiFi is managed through nm-applet in the system tray. Click the WiFi icon to connect to networks.

## Troubleshooting

### Common Issues

**Widgets not displaying properly:**
- Ensure `python-psutil` is installed: `sudo pacman -S python-psutil`
- Check qtile logs: `journalctl --user -u qtile`

**Wallpaper not loading:**
- Check wallpaper directory exists and contains images
- Verify path in `autostart.sh` is correct
- Ensure `feh` is installed: `sudo pacman -S feh`

**Keybindings not working:**
- Ensure qtile configuration loaded properly
- Check for syntax errors: `python -m py_compile ~/.config/qtile/config.py`
- Try reloading: Alt + Ctrl + r

**Services not starting:**
- Check if services are installed (picom, dunst, nm-applet)
- Verify autostart.sh is executable: `chmod +x ~/.config/qtile/autostart.sh`

### Testing Configuration
Always test config changes before restarting:
```bash
python -m py_compile ~/.config/qtile/config.py
```

Check qtile logs for errors:
```bash
journalctl --user -u qtile
```

## Dependencies

### Core Requirements
- `qtile` - Window manager
- `alacritty` - Terminal emulator
- `python-psutil` - For system monitoring widgets
- `ttf-jetbrains-mono` - Font

### Essential Utilities
- `feh` - Wallpaper setter and image viewer
- `rofi` - Application launcher
- `picom` - Compositor for effects
- `dunst` - Notification daemon
- `nm-applet` - Network management
- `pavucontrol` - Audio control

### Applications
- `qutebrowser` - Web browser
- `ranger` - File manager
- `neovim` - Text editor
- `zathura` - PDF viewer
- `mpv` - Media player
- `flameshot` - Screenshots

## Contributing

Feel free to fork this repository and adapt it to your needs. If you make improvements that could benefit others, pull requests are welcome!

## License

This configuration is provided as-is under the MIT license. Feel free to use and modify as needed.

## Acknowledgments

- Thanks to the qtile developers for an excellent tiling window manager
- Inspired by the gruvbox color scheme
- Built for the Arch Linux community

---

**Note**: This configuration is optimized for my personal workflow and hardware. You may want to adjust keybindings, applications, and layouts to match your preferences and system capabilities.
```
