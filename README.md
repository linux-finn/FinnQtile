```markdown
# FinnQtile

My personal qtile tiling window manager configuration for Arch Linux. A clean, functional setup optimized for productivity and daily workflow with **full cross-platform compatibility** for both laptops and desktops.

## 🖥️ Cross-Platform Features

This configuration intelligently adapts to your hardware:

- **🔋 Laptops**: Displays battery percentage, charge status, and battery icons
- **🔌 Desktops**: Shows power icon instead of battery widgets to prevent errors
- **⌨️ Consistent Super Key**: Windows key works on both laptop and desktop keyboards
- **🔍 Hardware Detection**: Automatically detects available hardware features
- **🎨 Nextcloud Integration**: Access to synchronized wallpaper collections across devices

## 📸 Screenshots

*Beautiful Gruvbox-themed desktop with intelligent status bar*

## ✨ Key Features

### 🎨 Visual Design
- **Font**: JetBrains Mono (size 16) for excellent readability
- **Color Scheme**: Gruvbox-inspired warm theme that's easy on the eyes
- **Status Bar**: Comprehensive system monitoring with hardware-adaptive widgets
- **Layouts**: Multiple tiling layouts optimized for different workflows

### 📊 Smart Status Bar Widgets

**Universal Widgets (All Systems):**
- **Current Layout** - Shows active window layout
- **Workspaces** - Clean numbered workspaces (1-9)
- **Window Name** - Current focused window title  
- **CPU Usage** - Real-time processor load percentage
- **Memory Usage** - Current RAM consumption with color coding
- **Network Monitor** - Upload/download speeds with directional arrows
- **Volume Control** - Current audio volume level
- **System Tray** - System notification icons (tested and working)
- **Clock** - UK format date/time (DD/MM/YYYY, 12-hour AM/PM)
- **Power Button** - Quick exit with confirmation dialog

**Hardware-Adaptive Widgets:**
- **🔋 Battery** (Laptops only) - Battery percentage with charging indicators
- **🔌 Power Icon** (Desktops) - Clean power status indicator

### 🚀 Application Integration
- **Terminal**: alacritty (fast GPU-accelerated terminal)
- **Browser**: qutebrowser (keyboard-driven browsing)
- **File Manager**: ranger (powerful terminal-based file manager)
- **Editor**: neovim (modern Vim experience)
- **PDF Viewer**: zathura (minimalist PDF viewer)
- **Media Player**: mpv (lightweight media player)
- **App Launcher**: rofi (beautiful application launcher)
- **Wallpaper Management**: feh + Nextcloud integration

### 🪟 Window Layouts
- **Columns**: Side-by-side tiling (default, excellent for productivity)
- **Max**: Single window fullscreen (focused work)
- **MonadTall**: Main window + side stack (coding with terminal)
- **Floating**: Traditional overlapping windows (dialogs, utilities)

### 🎨 Nextcloud Wallpaper Integration
- **Automatic Sync**: Wallpapers sync across all devices via Nextcloud
- **Random Selection**: Super + Shift + W cycles through your collection
- **Cross-Platform**: Same wallpaper collection on laptop and desktop
- **Large Collection Support**: Handles 100+ wallpapers efficiently

## 🚀 Installation

### 📋 Prerequisites

```bash
# Core qtile and terminal
sudo pacman -S qtile alacritty

# Essential applications
sudo pacman -S qutebrowser ranger neovim zathura mpv rofi

# Utilities and fonts
sudo pacman -S feh scrot ttf-jetbrains-mono dunst picom

# Network management
sudo pacman -S networkmanager network-manager-applet

# Optional: Nextcloud client for wallpaper sync
sudo pacman -S nextcloud-client
```

### ⚙️ Setup Instructions

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

3. **Set up Nextcloud wallpapers (optional):**
```bash
# Install and configure Nextcloud client
nextcloud &
# Follow setup wizard, sync your Wallpaper folder
```

4. **Configure wallpaper path:**
```bash
# Edit autostart.sh if needed for your wallpaper location
nano ~/.config/qtile/autostart.sh
```

5. **Test configuration:**
```bash
python -m py_compile ~/.config/qtile/config.py
```

6. **Enable services:**
```bash
sudo systemctl enable lightdm  # or your preferred display manager
sudo systemctl enable NetworkManager
```

7. **Log into qtile from your display manager**

## ⌨️ Keybindings Reference

### 🪟 Window Management
| Keybinding | Action |
|---|---|
| `Super + Return` | Open terminal (alacritty) |
| `Super + d` | Launch rofi application launcher |
| `Super + w` | Close focused window |
| `Super + f` | Toggle fullscreen |
| `Super + t` | Toggle floating mode |

### 🚀 Application Shortcuts
| Keybinding | Application |
|---|---|
| `Super + b` | qutebrowser (web browser) |
| `Super + e` | ranger (file manager) |
| `Super + v` | neovim (text editor) |
| `Super + m` | mpv (media player) |
| `Super + z` | zathura (PDF viewer) |
| `Super + s` | Screenshot (selection mode) |

### 🎨 Wallpaper Management
| Keybinding | Action |
|---|---|
| `Super + Shift + w` | **Random wallpaper from Nextcloud collection** |

### 🧭 Navigation
| Keybinding | Action |
|---|---|
| `Super + h/j/k/l` | Move focus left/down/up/right (vim-style) |
| `Super + Shift + h/j/k/l` | Move window left/down/up/right |
| `Super + Ctrl + h/j/k/l` | Resize window in direction |
| `Super + n` | Reset all window sizes |
| `Super + Space` | Move to next window |

### 🏢 Workspaces & Layouts
| Keybinding | Action |
|---|---|
| `Super + Tab` | Switch between layouts |
| `Super + 1-9` | Switch to workspace 1-9 |
| `Super + Shift + 1-9` | Move window to workspace 1-9 |

### ⚙️ System Controls
| Keybinding | Action |
|---|---|
| `Super + Ctrl + r` | **Reload qtile configuration** |
| `Super + Ctrl + q` | Quit qtile |
| `Super + r` | Qtile command prompt |

## 💡 Usage Tips & Workflow

### 📁 Recommended Workspace Organization:
- **Workspace 1**: Terminal work and system tasks
- **Workspace 2**: Web browsing (qutebrowser)
- **Workspace 3**: File management (ranger)
- **Workspace 4**: Coding and development (neovim)
- **Workspace 5**: Media and entertainment (mpv)

### ⚡ Efficient Navigation Tips:
- Use `Super + number` for lightning-fast workspace switching
- Master `Super + h/j/k/l` for vim-like window navigation
- `Super + d` + type for instant application launching
- `Super + Shift + w` for instant visual refresh with new wallpapers

### 🔧 Layout Management Strategy:
- **Start with Columns** layout for most productive work
- **Switch to Max** for focused, distraction-free tasks
- **Use MonadTall** for coding (editor + terminal combo)
- **Use Floating** for dialogs, settings, and special windows

### 🎨 Wallpaper Management:
- Sync your wallpaper collection via Nextcloud for cross-device access
- Use `Super + Shift + w` to instantly refresh your desktop aesthetic
- Wallpapers automatically scale to fit your screen resolution

## 🎨 Customization Guide

### 🌈 Color Scheme
Edit the `colors` dictionary in `config.py`:
```python
colors = {
    'bg': '#282828',        # Background - warm dark
    'fg': '#ebdbb2',        # Foreground - cream white
    'blue': '#458588',      # Accent - calming blue
    'green': '#98971a',     # Success - natural green
    'yellow': '#d79921',    # Warning - warm yellow
    'red': '#cc241d',       # Error - muted red
    # ... customize other colors
}
```

### ⌨️ Custom Keybindings
Add new keybindings in the `keys` list:
```python
Key([mod], "key", lazy.spawn("application"), desc="Description"),
Key([mod, "shift"], "key", lazy.function(), desc="Custom function"),
```

### 📊 Widget Customization
Modify the `screens` section to add/remove/reorder widgets:
```python
# Add new widgets to the bar
widget.YourWidget(
    format='Custom format',
    foreground=colors['purple'],
    update_interval=5
),
```

### 🚀 Autostart Applications
Edit `autostart.sh` to launch applications at startup:
```bash
# Add your applications
discord &
spotify &
code &
```

## 🔧 Troubleshooting

### Common Issues & Solutions

**Keybindings not working:**
- Ensure qtile loaded properly: `Super + Ctrl + r` to reload
- Check for conflicting window managers
- Verify Super key mapping with UK keyboard layout

**Wallpapers not changing:**
- Verify Nextcloud sync: `ls ~/Nextcloud/Wallpaper/`
- Test manually: `feh --bg-scale --randomize ~/Nextcloud/Wallpaper/*`
- Check file permissions and path in config

**System tray issues:**
- Install required packages: `sudo pacman -S network-manager-applet`
- Check if other tray apps work: `nm-applet &`
- Verify `widget.Systray()` is in your bar configuration

**Battery widget errors on desktop:**
- This config automatically detects hardware and shows appropriate widgets
- Desktops show power icon instead of battery widget

### 🧪 Testing Configuration Changes
Always test config changes before restarting:
```bash
python -m py_compile ~/.config/qtile/config.py
```

View qtile logs for debugging:
```bash
journalctl --user -u qtile --no-pager | tail -20
```

### 🔑 Super Key Issues
If Super key doesn't work properly:
```bash
# Check key mapping
xmodmap -pm | grep -i super

# Reset key mapping (already handled in autostart)
setxkbmap -option altwin:swap_alt_win
```

## 📦 Dependencies & Requirements

### 🔧 Core Requirements:
- `qtile` - Tiling window manager
- `alacritty` - Terminal emulator
- `ttf-jetbrains-mono` - Primary font
- `feh` - Wallpaper management
- `python` - Configuration language

### 🚀 Essential Applications:
- `rofi` - Application launcher
- `qutebrowser` - Web browser
- `ranger` - File manager
- `neovim` - Text editor
- `zathura` - PDF viewer
- `mpv` - Media player
- `scrot` - Screenshot utility

### 🔌 System Integration:
- `dunst` - Notification daemon
- `picom` - Compositor for effects
- `networkmanager` - Network management
- `network-manager-applet` - System tray networking

### 🎨 Optional Enhancements:
- `nextcloud-client` - Wallpaper sync across devices
- `pavucontrol` - Audio control
- `blueman` - Bluetooth management

## 🤝 Contributing

Feel free to fork this repository and adapt it to your needs! If you make improvements that could benefit others:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your improvements
4. **Test** thoroughly on both laptop and desktop
5. **Submit** a pull request

### 🎯 Areas for Contribution:
- Additional hardware detection (multiple monitors, etc.)
- New application integrations
- Alternative color schemes
- Performance optimizations
- Documentation improvements

## 📄 License

This configuration is provided as-is under the **MIT License**. Feel free to use, modify, and distribute as needed.

## 🙏 Acknowledgments

- **Qtile developers** for creating an excellent Python-based tiling window manager
- **Gruvbox color scheme** for the beautiful, eye-friendly palette
- **Arch Linux community** for maintaining excellent packages
- **JetBrains** for the fantastic JetBrains Mono font
- **Nextcloud** for seamless file synchronization across devices

## 🌟 Special Features

### 🔄 Cross-Platform Intelligence
This configuration automatically detects your hardware and adapts:
- Laptop detection via battery presence
- Keyboard mapping normalization
- Widget selection based on available hardware

### 🎨 Aesthetic Excellence
- Carefully chosen Gruvbox color palette
- Consistent visual hierarchy
- Beautiful typography with JetBrains Mono
- Smooth transitions and effects

### ⚡ Performance Optimized
- Lightweight widget selection
- Efficient update intervals
- Minimal resource usage
- Fast startup times

---

**Note**: This configuration is battle-tested on both laptop and desktop environments. It automatically adapts to your hardware while maintaining a consistent, beautiful, and productive experience across all your devices.

**Quick Start**: Clone, copy configs, test compilation, and enjoy your new productive workspace! 🚀
```
