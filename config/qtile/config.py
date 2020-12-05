from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from typing import List
import os


mod = "mod4"
alt = "mod1"
terminal = "kitty"
browser = "firefox"
user = "sasha"
color = [
    "#FFFFFF",  # 0. Text color
    "#CED4DA",  # 1. Unfocus color
    "#008DCD",  # 2. Focus color
    "#262A2B",  # 3. Panel color
    "#51AFEF",  # 4. Text color
    "#C678DD",  # 5. Text color
    "#FF6C6B",  # 6. Text color
    "#ECBE7B",  # 7. Text color
    "#98BE65",  # 8. Text color
]


@hook.subscribe.startup_once
def autostart(): os.system("~/.config/qtile/autostart.sh")


keys = [
    # Applications
    Key([mod], "Return",
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
    Key([mod], "F2",
        lazy.spawn(browser),
        desc="Launch browser"
    ),
    Key([mod, alt], "t",
        lazy.spawn(f"{terminal} -e \"nvim /home/{user}/.todo\""),
        desc="Open ~/.todo file in nvim"
    ),

    # Window control 
    Key([mod], "q", 
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Change focus window(left)"
    ),
    Key([mod], "j",
        lazy.layout.down(), 
        desc="Change focus window(down)"
    ),
    Key([mod], "k", 
        lazy.layout.up(),
        desc="Change focus window(up)"
    ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Change focus window(right)"
    ),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move focus window(left)"
    ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move focus window(down)"
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move focus window(up)"
    ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move focus window(right)"
    ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        #lazy.layout.grow()),
        desc="Resize focus window(left)"
    ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Resize focus window(down)"
    ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Resize focus window(up)"
    ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        #lazy.layout.shrink()
        desc="Resize focus window(right)"
    ),

    # Layout
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"
    ),
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        desc="Swap panes of split stack"
    ),

    # Volume
    Key([mod], "equal",
        lazy.spawn("pactl set-sink-volume alsa_output.pci-0000_00_1b.0.analog-stereo +2%"),
        desc="Plus 2% volume"
    ),
    Key([mod], "minus",
        lazy.spawn("pactl set-sink-volume alsa_output.pci-0000_00_1b.0.analog-stereo -2%"),
        desc="Minus 2% volume"
    ),
    Key([mod, "shift"], "minus",
        lazy.spawn("pactl set-sink-mute alsa_output.pci-0000_00_1b.0.analog-stereo toggle"),
        desc="Mute volume"
    ),

    # Menus(dmenu & rofi) 
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show drun -drun-display-format \"{name}\""),
        desc="(Rofi) Program launcher"
    ),
    Key([mod],"Escape",
        lazy.spawn(f"/home/{user}/.script/dmenu/dmenu-power.sh"),
        desc="Power menu"
    ),
    Key([mod, "control"], "i",
        lazy.spawn("passmenu -h 24 -p Password"),
        desc="Dmenu password menu"
    ),
    Key([mod, "control"], "u",
        lazy.spawn(f"/home/{user}/.script/dmenu/dmenu-config-edit.sh"),
        desc="Config editor"
    ),
    Key([mod, "control"], "o",
        lazy.spawn(f"/home/{user}/.script/dmenu/dmenu-sysmon.sh"),
        desc="Choice system monitor"
    ),

    # Screenhot
    Key([], "Print",
        lazy.spawn(f"scrot -s /home/{user}/$(date +%Y-%m-%d-%H-%M-%S).png"),
        desc="Create screenhot(scrot -s)"
    ),
    Key(["shift"], "Print",
        lazy.spawn(f"scrot /home/{user}/$(date +%Y-%m-%d-%H-%M-%S).png"),
        desc="Create screenhot full screen(scrot)"
    ),

    # Qtile
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart qtile"
    ),
    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
    ),
]

# Workspaces name, keys
group_names = [("term", {'layout': 'monadtall'}),
               ("www",  {'layout': 'max'}),
               ("dev",  {'layout': 'monadtall'}),
               ("sys",  {'layout': 'monadtall'}),
               ("doc",  {'layout': 'monadtall'}),
               ("chat", {'layout': 'monadtall'}),
               ("pass", {'layout': 'monadtall'}),
               ("mus",  {'layout': 'max'}),
               ("flo",  {'layout': 'monadtall'})
]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# Window layout(s)
layout_theme = {
    "border_width": 1,
    "margin": 3,
    "border_focus": color[2],
    "border_normal": color[1],
    "font": "Jatbrains Mono"
}
layouts = [
    layout.Max(),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    layout.Columns(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(), 
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Panel
widget_defaults = dict(
    font='Jatbrains Mono',
    fontsize=12,
    padding=5,
    foreground=color[0],
    background=color[3],
)
extension_defaults = widget_defaults.copy()
screens = [Screen(top=bar.Bar([
    widget.GroupBox(
        active=color[0],
        inactive=color[1],
        rounded=False,
        disable_drag=True,
        highlight_color=color[2],
        highlight_method="block",
        this_current_screen_border=color[2],
        this_screen_border=color[3],
        foreground=color[0],
    ),
    widget.Prompt(foreground=color[0]),
    widget.WindowName(foreground=color[0]),
    widget.KeyboardKbdd(
        foreground=color[5],
        configured_keyboards=['us', 'ru', 'ua'],
        update_interval=0,
        fmt=" {}",
    ),
    widget.CurrentLayout(
        foreground=color[8]
    ),
    widget.Volume(
        foreground=color[6],
        fmt=" {}",
    ),
    widget.Net(
        interface="wlp3s0",
        format='{down}↓↑{up}',
        foreground=color[7],
    ),
    widget.Systray(),
    widget.Clock(
        format=' %H:%M',
        foreground=color[4]
    ),
    widget.Clock(
        format=" %d.%m.%Y",
        foreground=color[4]
    )], 24 # Panel size 
))]

# Drag floating layouts
mouse = [
    Drag([mod],  "Button1", lazy.window.set_position(), start=lazy.window.get_position()),
    Drag([mod],  "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wname':   'branchdialog'},
    {'wname':   'pinentry'},
    {'wmclass': 'ssh-askpass'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"