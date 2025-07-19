```markdown
# FinnQtile

My personal qtile tiling window manager configuration for Arch Linux. A clean, functional setup optimized for productivity and daily workflow with **cross-platform compatibility** for both laptops and desktops.

## 🖥️ Cross-Platform Features

This configuration automatically adapts to your hardware:

- **Laptops**: Shows battery percentage, charge status, and battery icons
- **Desktops**: Shows power icon instead of battery widgets
- **Consistent Super Key**: Windows key works on both laptop and desktop keyboards
- **Hardware Detection**: Automatically detects available hardware features

## Screenshots

*Add screenshots of your setup here*

## ✨ Features

### Visual Design
- **Font**: JetBrains Mono (size 16)
- **Color Scheme**: Gruvbox-inspired theme with warm, easy-on-the-eyes colors
- **Status Bar**: Comprehensive system monitoring with hardware-adaptive widgets
- **Layouts**: Multiple tiling layouts for different workflow needs

### Smart Status Bar Widgets

**Universal Widgets (All Systems):**
- **Current Layout** - Shows active window layout
- **Workspaces** - Clean numbered workspaces (1-9)
- **Window Name** - Current focused window title
- **CPU Usage** - Real-time processor load percentage
- **Memory Usage** - Current RAM consumption
- **Network** - Upload/download speeds with arrows
- **Volume** - Current audio volume level
- **System Tray** - System notification icons
- **Clock** - UK format date/time (DD/MM/YYYY, 12-hour AM/PM)
- **Power Button** - Quick exit with confirmation

**Hardware-Adaptive Widgets:**
- **Battery** (Laptops only) - Battery percentage with charging indicators
- **Power Icon** (Desktops) - Power status indicator

### Application Integration
- **Terminal**: alacritty
- **Browser**: qutebrowser
- **File Manager**: ranger (terminal-based)
- **Editor**: neovim
- **PDF Viewer**: zathura
- **Media Player**: mpv
- **App Launcher**: rofi (beautiful grid layout)

### Window Layouts
- **Columns**: Side-by-side tiling (default)
- **Max**: Single window fullscreen
- **MonadTall**: Main window + side stack
- **Floating**: Traditional overlapping windows

## 🚀 Installation

### Prerequisites

```bash
# Install qtile and dependencies
sudo pacman -S qtile alacritty

# Install applications
sudo pacman -S qutebrowser ranger neovim zathura mpv rofi

# Install utilities
sudo pacman -S feh scrot ttf-jetbrains-mono

# Optional: for screenshots
sudo pacman -S scrot
```

### Setup

1. **Clone this repository:**
```bash
git clone https://github.com/linux-finn/FinnQtile.git
cd FinnQtile
```

2. **Install configuration:**
```bash
# Create qtile config directory
mkdir -p ~/.config/qtile

# Copy configuration files
cp config.py ~/.config/qtile/
cp autostart.sh ~/.config/qtile/
chmod +x ~/.config/qtile/autostart.sh
```

3. **Set your wallpaper path:**
```bash
# Edit autostart.sh and update wallpaper path
nano ~/.config/qtile/autostart.sh
```

4. **Test configuration:**
```bash
python -m py_compile ~/.config/qtile/config.py
```

5. **Log into qtile from your display manager**

## ⌨️ Keybindings

### Window Management
| Keybinding | Action |
|---|---|
| `Super + Return` | Open terminal |
| `Super + d` | Launch rofi application launcher |
| `Super + w` | Close window |
| `Super + f` | Toggle fullscreen |
| `Super + t` | Toggle floating mode |

### Application Shortcuts
| Keybinding | Application |
|---|---|
| `Super + b` | qutebrowser |
| `Super + e` | ranger (file manager) |
| `Super + v` | neovim |
| `Super + m` | mpv |
| `Super + z` | zathura (PDF viewer) |
| `Super + s` | Screenshot (selection) |

### Navigation
| Keybinding | Action |
|---|---|
| `Super + h/j/k/l` | Move focus left/down/up/right |
| `Super + Shift + h/j/k/l` | Move window left/down/up/right |
| `Super + Ctrl + h/j/k/l` | Resize window |
| `Super + n` | Reset window sizes |
| `Super + Space` | Move to next window |

### Workspaces & Layouts
| Keybinding | Action |
|---|---|
| `Super + Tab` | Switch between layouts |
| `Super + 1-9` | Switch to workspace 1-9 |
| `Super + Shift + 1-9` | Move window to workspace 1-9 |

### System Controls
| Keybinding | Action |
|---|---|
| `Super + Ctrl + r` | Reload qtile configuration |
| `Super + Ctrl + q` | Quit qtile |
| `Super + r` | Qtile command prompt |

## 💡 Usage Tips

### Workspace Organization:
- Workspace 1: Terminal work
- Workspace 2: Web browsing
- Workspace 3: File management
- Workspace 4: Coding/development
- Workspace 5: Media/entertainment

### Efficient Navigation:
- Use `Super + number` for quick workspace switching
- Use `Super + h/j/k/l` for vim-like window navigation
- Use `Super + d` for quick app launching with rofi

### Layout Management:
- Start with Columns layout for most tasks
- Switch to Max for focused work
- Use MonadTall for coding with terminal + editor
- Use Floating for dialogs and special windows

## 🎨 Customization

### Colors
Edit the `colors` dictionary in `config.py`:
```python
colors = {
    'bg': '#282828',        # Background
    'fg': '#ebdbb2',        # Foreground
    'blue': '#458588',      # Accent color
    # ... other colors
}
```

### Keybindings
Add new keybindings in the `keys` list:
```python
Key([mod], "key", lazy.spawn("application"), desc="Description"),
```

### Widgets
Modify the `screens` section to add/remove widgets or change their order.

### Autostart Applications
Edit `autostart.sh` to launch applications at startup:
```bash
discord &
spotify &
```

## 🔧 Troubleshooting

- **Keybindings not working**: Ensure qtile is properly loaded and no other WM is interfering
- **Wallpaper not loading**: Check file path in `autostart.sh`
- **Widgets not displaying**: Some widgets require specific packages
- **Super key issues**: The config includes automatic key mapping for different keyboards

### Testing Config Changes
Always test config changes before restarting:
```bash
python -m py_compile ~/.config/qtile/config.py
```

Check qtile logs for errors:
```bash
journalctl --user -u qtile
```

## 📦 Dependencies

### Core Requirements:
- `qtile` - Window manager
- `alacritty` - Terminal emulator
- `ttf-jetbrains-mono` - Font
- `feh` - Wallpaper setter
- `python` - For qtile configuration

### Applications:
- `rofi` - Application launcher
- `qutebrowser` - Web browser
- `ranger` - File manager
- `neovim` - Text editor
- `zathura` - PDF viewer
- `mpv` - Media player
- `scrot` - Screenshots

## 🤝 Contributing

Feel free to fork this repository and adapt it to your needs. If you make improvements that could benefit others, pull requests are welcome!

## 📄 License

This configuration is provided as-is under the MIT license. Feel free to use and modify as needed.

## 🙏 Acknowledgments

- Thanks to the qtile developers for an excellent tiling window manager
- Inspired by the gruvbox color scheme
- Built for the Arch Linux community

---

**Note**: This configuration automatically detects your hardware and adapts accordingly. It works seamlessly on both laptops and desktop computers without manual modification.
```
