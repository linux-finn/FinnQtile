```markdown
# FinnQtile

My personal qtile tiling window manager configuration for Arch Linux. A clean, functional setup optimized for productivity and daily workflow.

## Screenshots
*Add screenshots of your setup here*

## Features

### Visual Design
- **Font**: JetBrains Mono (size 16)
- **Color Scheme**: Gruvbox-inspired theme with warm, easy-on-the-eyes colors
- **Status Bar**: Comprehensive system monitoring with all essential widgets
- **Layouts**: Multiple tiling layouts for different workflow needs

### Status Bar Widgets
- **Current Layout** - Shows active window layout
- **Workspaces** - Clean numbered workspaces (1-9)
- **Window Name** - Current focused window title
- **CPU Usage** - Real-time processor load percentage
- **Memory Usage** - Current RAM consumption
- **Network** - Upload/download speeds with arrows
- **Volume** - Current audio volume level
- **Battery** - Battery percentage with charging indicators
- **System Tray** - System notification icons
- **Clock** - UK format date/time (DD/MM/YYYY, 12-hour AM/PM)
- **Power Button** - Quick exit with confirmation

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

## Installation

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
   git clone https://github.com/yourusername/FinnQtile.git
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

## Key Bindings

### Essential Keys
| Keybinding | Action |
|------------|--------|
| `Super + Return` | Open terminal |
| `Super + d` | Launch rofi application launcher |
| `Super + w` | Close window |
| `Super + f` | Toggle fullscreen |
| `Super + t` | Toggle floating mode |

### Applications
| Keybinding | Application |
|------------|-------------|
| `Super + b` | qutebrowser |
| `Super + e` | ranger (file manager) |
| `Super + v` | neovim |
| `Super + m` | mpv |
| `Super + z` | zathura (PDF viewer) |
| `Super + s` | Screenshot (selection) |

### Window Management
| Keybinding | Action |
|------------|--------|
| `Super + h/j/k/l` | Move focus left/down/up/right |
| `Super + Shift + h/j/k/l` | Move window left/down/up/right |
| `Super + Ctrl + h/j/k/l` | Resize window |
| `Super + n` | Reset window sizes |
| `Super + Space` | Move to next window |

### Layouts & Workspaces
| Keybinding | Action |
|------------|--------|
| `Super + Tab` | Switch between layouts |
| `Super + 1-9` | Switch to workspace 1-9 |
| `Super + Shift + 1-9` | Move window to workspace 1-9 |

### System Controls
| Keybinding | Action |
|------------|--------|
| `Super + Ctrl + r` | Reload qtile configuration |
| `Super + Ctrl + q` | Quit qtile |
| `Super + r` | Qtile command prompt |

## Workflow Tips

### Daily Usage
1. **Workspace Organization:**
   - Workspace 1: Terminal work
   - Workspace 2: Web browsing
   - Workspace 3: File management
   - Workspace 4: Coding/development
   - Workspace 5: Media/entertainment

2. **Efficient Navigation:**
   - Use `Super + number` for quick workspace switching
   - Use `Super + h/j/k/l` for vim-like window navigation
   - Use `Super + d` for quick app launching with rofi

3. **Layout Management:**
   - Start with Columns layout for most tasks
   - Switch to Max for focused work
   - Use MonadTall for coding with terminal + editor
   - Use Floating for dialogs and special windows

## Customization

### Changing Colors
Edit the `colors` dictionary in `config.py`:
```python
colors = {
    'bg': '#282828',     # Background
    'fg': '#ebdbb2',     # Foreground
    'blue': '#458588',   # Accent color
    # ... other colors
}
```

### Adding Applications
Add new keybindings in the `keys` list:
```python
Key([mod], "key", lazy.spawn("application"), desc="Description"),
```

### Status Bar Widgets
Modify the `screens` section to add/remove widgets or change their order.

### Autostart Applications
Edit `autostart.sh` to launch applications at startup:
```bash
discord &
spotify &
```

## Troubleshooting

### Common Issues
- **Keybindings not working**: Ensure qtile is properly loaded and no other WM is interfering
- **Wallpaper not loading**: Check file path in `autostart.sh`
- **Widgets not displaying**: Some widgets require specific packages (e.g., battery widget on laptops only)

### Testing Configuration
Always test config changes before restarting:
```bash
python -m py_compile ~/.config/qtile/config.py
```

### Logs
Check qtile logs for errors:
```bash
journalctl --user -u qtile
```

## Dependencies

### Required Packages
- `qtile` - Window manager
- `alacritty` - Terminal emulator
- `ttf-jetbrains-mono` - Font
- `feh` - Wallpaper setter
- `python` - For qtile configuration

### Optional Packages
- `rofi` - Application launcher
- `qutebrowser` - Web browser
- `ranger` - File manager
- `neovim` - Text editor
- `zathura` - PDF viewer
- `mpv` - Media player
- `scrot` - Screenshots

## Contributing

Feel free to fork this repository and adapt it to your needs. If you make improvements that could benefit others, pull requests are welcome!

## License

This configuration is provided as-is under the MIT license. Feel free to use and modify as needed.

## Acknowledgments

- Thanks to the qtile developers for an excellent tiling window manager
- Inspired by the gruvbox color scheme
- Built for the Arch Linux community

---

**Note**: This configuration is optimized for my personal workflow. You may want to adjust keybindings, applications, and layouts to match your preferences.
```
