# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import subprocess
import os

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
    
    # Move windows between left/right columns or move up/down in current stack
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
    
    # Toggle between split and unsplit sides of stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
    # Launch applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("qutebrowser"), desc="Launch qutebrowser"),
    Key([mod], "e", lazy.spawn(terminal + " -e ranger"), desc="Launch ranger file manager"),
    Key([mod], "v", lazy.spawn(terminal + " -e nvim"), desc="Launch neovim"),
    Key([mod], "m", lazy.spawn("mpv"), desc="Launch mpv"),
    Key([mod], "z", lazy.spawn("zathura"), desc="Launch zathura PDF viewer"),
    Key([mod, "shift"], "h", lazy.spawn(terminal + " -e htop"), desc="Launch htop"),
    
    # Layout and window controls
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    
    # Qtile controls
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("dmenu_run -fn 'JetBrains Mono:size=16' -nb '" + colors['bg'] + "' -nf '" + colors['fg'] + "' -sb '" + colors['blue'] + "' -sf '" + colors['bg'] + "'"), desc="Launch dmenu"),
    
    # Volume controls
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute volume"),
    
    # Brightness controls
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease brightness"),
    
    # Screenshot
    Key([mod], "s", lazy.spawn("scrot -s"), desc="Take screenshot"),
]

# Add key bindings to switch VTs in Wayland
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            # mod + shift + group number = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}"),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack=[colors['blue'], colors['aqua']], 
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
        top=bar.Bar(
            [
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
                widget.WindowName(
                    foreground=colors['fg'],
                    max_chars=50
                ),
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
                    update_interval=0.1
                ),
                widget.Sep(
                    linewidth=2,
                    foreground=colors['gray'],
                    padding=10
                ),
                widget.Battery(
                    format='{percent:2.0%} {char}',
                    foreground=colors['aqua'],
                    update_interval=60,
                    charge_char='⚡',
                    discharge_char='🔋',
                    full_char='🔋'
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
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    foreground=colors['blue'],
                    padding=10
                ),
                widget.QuickExit(
                    default_text='⏻',
                    countdown_format='{}',
                    foreground=colors['red'],
                    padding=10
                ),
            ],
            30,
            background=colors['bg'],
            opacity=0.95
        ),
    ),
]

# Drag floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
    border_focus=colors['blue'],
    border_normal=colors['gray'],
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="mpv"),
        Match(wm_class="zathura"),
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
