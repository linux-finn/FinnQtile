from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess
import os

# Detect if we have a battery (laptop vs desktop)
def has_battery():
    return os.path.exists('/sys/class/power_supply/BAT0') or os.path.exists('/sys/class/power_supply/BAT1')

mod = "mod4"
terminal = "alacritty"

# Color scheme
colors = {
    'bg': '#282828',
    'fg': '#ebdbb2',
    'red': '#cc241d',
    'green': '#98971a',
    'yellow': '#d79921',
    'blue': '#458588',
    'purple': '#b16286',
    'aqua': '#689d6a',
    'gray': '#a89984',
    'orange': '#d65d0e'
}

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Launch applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("qutebrowser"), desc="Launch qutebrowser"),
    Key([mod], "e", lazy.spawn("alacritty -e ranger"), desc="Launch ranger file manager"),
    Key([mod], "v", lazy.spawn("alacritty -e nvim"), desc="Launch neovim"),
    Key([mod], "m", lazy.spawn("mpv"), desc="Launch mpv"),
    Key([mod], "z", lazy.spawn("zathura"), desc="Launch zathura PDF viewer"),
    
    # Layout and window controls
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    
    # Qtile controls
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    
    # Screenshot
    Key([mod], "s", lazy.spawn("scrot -s"), desc="Take screenshot"),
    
    # Wallpaper changer - Updated for Nextcloud
    Key([mod, "shift"], "w", lazy.spawn("sh -c 'feh --bg-scale --randomize ~/Nextcloud/Wallpaper/*'"), desc="Random wallpaper"),
]

# Numbered workspaces
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

# Layout options
layouts = [
    layout.Columns(
        border_width=2,
        border_focus=colors['blue'],
        border_normal=colors['gray'],
        margin=4
    ),
    layout.Max(),
    layout.MonadTall(
        border_focus=colors['blue'],
        border_normal=colors['gray'],
        border_width=2,
        margin=4
    ),
    layout.Floating(
        border_focus=colors['blue'],
        border_normal=colors['gray'],
        border_width=2
    ),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=16,
    padding=3,
    foreground=colors['fg'],
    background=colors['bg']
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
            widget.CurrentLayout(
                foreground=colors['yellow'],
                padding=10
            ),
            widget.GroupBox(
                active=colors['fg'],
                inactive=colors['gray'],
                this_current_screen_border=colors['blue'],
                this_screen_border=colors['aqua'],
                urgent_alert_method='block',
                urgent_border=colors['red'],
                padding=5,
                margin=3,
                borderwidth=2,
                rounded=False,
                highlight_method='border'
            ),
            widget.WindowName(),
            widget.Spacer(),
            widget.CPU(
                format='CPU: {load_percent}%',
                foreground=colors['green'],
                update_interval=2
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.Memory(
                format='RAM: {MemUsed:.0f}M',
                foreground=colors['yellow'],
                update_interval=2
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.Net(
                format='{down} ↓↑ {up}',
                foreground=colors['purple'],
                update_interval=3
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.Volume(
                foreground=colors['orange'],
                fmt='Vol: {}',
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            *(
                [widget.Battery(
                    format='{percent:2.0%} {char}',
                    foreground=colors['aqua'],
                    update_interval=60,
                    charge_char='⚡',
                    discharge_char='🔋',
                    full_char='🔋'
                )] if has_battery() else [
                    widget.TextBox(
                        text='🔌',
                        foreground=colors['aqua'],
                        fontsize=20,
                        padding=10
                    )
                ]
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.Systray(
                padding=5
            ),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.Clock(format='%d/%m/%Y %a %I:%M %p', foreground=colors['blue']),
            widget.Sep(
                linewidth=2,
                foreground=colors['gray'],
                padding=10
            ),
            widget.QuickExit(
                default_text='⏻',
                countdown_format='{}',
                foreground=colors['red'],
                padding=10
            ),
        ], 30, background=colors['bg']),
    ),
]

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(['feh', '--bg-fill', '/home/linuxfinn/Downloads/Arch Wallpaper.png'])
    subprocess.Popen(['dunst'])
    subprocess.Popen(['picom'])
    subprocess.Popen(['nextcloud'])
    subprocess.Popen(['setxkbmap', '-option', 'altwin:swap_alt_win'])

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating()),
    Drag([mod], "Button3", lazy.window.set_size_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    border_focus=colors['blue'],
    border_normal=colors['gray'],
    border_width=2
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"
