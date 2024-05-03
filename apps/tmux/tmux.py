from talon import Context, Module, actions, settings

mod = Module()

mod.apps.tmux = """
tag: terminal
and tag: user.tmux
"""

mod.setting(
    "tmux_prefix_key",
    type=str,
    default="ctrl-b",
    desc="The key used to prefix all tmux commands",
)


@mod.action_class
class TmuxActions:
    def tmux_prefix(self):
        """press control and the configured tmux prefix key"""
        actions.key(settings.get("user.tmux_prefix_key"))

    def tmux_keybind(key: str):
        """press tmux prefix followed by a key bind"""
        actions.user.tmux_prefix()
        actions.key(key)

    def tmux_enter_command(command: str = ""):
        """Enter tmux command mode and optionally insert a command without executing it."""
        actions.user.tmux_keybind(":")
        actions.insert(command)

    def tmux_execute_command(command: str):
        """execute tmux command"""
        actions.user.tmux_enter_command(command)
        actions.key("enter")
        actions.sleep("100ms")

    def tmux_execute_command_with_confirmation(command: str, confirmation_prompt: str):
        """execute tmux command with confirm-before"""
        actions.user.tmux_execute_command(
            f'confirm-before -p "{confirmation_prompt} (y/n)" {command}'
        )
        actions.key("\n")


ctx = Context()
ctx.matches = "app: tmux"


@ctx.action_class("app")
class AppActions:
    def tab_open(self):
        actions.user.tmux_execute_command("new-window")

    def tab_next(self):
        actions.user.tmux_execute_command("select-window -n")

    def tab_previous(self):
        actions.user.tmux_execute_command("select-window -p")


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number < 10:
            actions.user.tmux_keybind(f"{number}")
        else:
            actions.user.tmux_execute_command(f"select-window -t {number}")

    def tab_close_wrapper(self):
        actions.user.tmux_execute_command_with_confirmation(
            "kill-window", "kill-window #W?"
        )

    def split_window_right(self):
        actions.user.split_window_horizontally()
        actions.user.tmux_execute_command("swap-pane -U -s #P")

    def split_window_left(self):
        actions.user.split_window_horizontally()

    def split_window_down(self):
        actions.user.split_window_vertically()
        actions.user.tmux_execute_command("swap-pane -U -s #P")

    def split_window_up(self):
        actions.user.split_window_vertically()

    def split_flip(self):
        actions.user.tmux_execute_command("next-layout")

    def split_window_vertically(self):
        actions.user.tmux_execute_command("split-pane")

    def split_window_horizontally(self):
        actions.user.tmux_execute_command("split-pane -h")

    def split_maximize(self):
        # toggle the maximization because zooming when already zoomed is pointless
        actions.user.tmux_execute_command("resize-pane -Z")

    def split_reset(self):
        actions.user.tmux_execute_command("resize-pane -Z")

    def split_window(self):
        actions.user.split_window_horizontally()

    def split_clear(self):
        actions.user.tmux_execute_command_with_confirmation(
            "kill-pane", "kill-pane #P?"
        )

    def split_next(self):
        # select-pane doesn't seem to support the prefix-o behavior
        actions.user.tmux_keybind("o")

    def split_last(self):
        actions.user.tmux_execute_command("select-pane -l")

    def split_number(index: int):
        actions.user.tmux_execute_command(f"select-pane -t {index}")
