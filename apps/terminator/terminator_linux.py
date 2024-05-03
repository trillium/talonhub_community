from talon import Context, Module, actions

# App definition
mod = Module()
mod.apps.terminator = """
os: linux
and app.exe: terminator
os: linux
and app.name: Terminator
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: terminator
"""
ctx.tags = [
    "terminal",
    "user.tabs",
    "user.splits",
    "user.generic_unix_shell",
    "user.git",
    "user.kubectl",
]


# --- Implement actions ---
@ctx.action_class("user")
class user_actions:
    # user.splits
    def split_window_right(self):
        actions.key("alt-right")

    def split_window_left(self):
        actions.key("alt-left")

    def split_window_down(self):
        actions.key("alt-down")

    def split_window_up(self):
        actions.key("alt-up")

    def split_window_vertically(self):
        actions.key("shift-ctrl-e")

    def split_window_horizontally(self):
        actions.key("shift-ctrl-o")

    def split_flip(self):
        actions.key("super-r")

    def split_maximize(self):
        actions.key("shift-ctrl-x")

    def split_reset(self):
        actions.key("shift-ctrl-x")

    def split_window(self):
        actions.key("shift-ctrl-o")

    def split_clear(self):
        actions.key("shift-ctrl-r")

    def split_clear_all(self):
        actions.key("shift-ctrl-g")

    def split_next(self):
        actions.key("shift-ctrl-n")

    def split_last(self):
        actions.key("shift-ctrl-p")


@ctx.action_class("app")
class AppActions:
    # app.tabs
    def tab_open(self):
        actions.key("ctrl-shift-t")

    def tab_previous(self):
        actions.key("ctrl-pageup")

    def tab_next(self):
        actions.key("ctrl-pagedown")

    def tab_close(self):
        actions.key("ctrl-shift-w")

    # global (overwrite linux/app.py)
    def window_open(self):
        actions.key("ctrl-shift-i")

    def window_close(self):
        actions.key("ctrl-shift-q")


# global (overwrite linux/edit.py)
@ctx.action_class("edit")
class EditActions:
    def page_down(self):
        actions.key("shift-pagedown")

    def page_up(self):
        actions.key("shift-pageup")

    def paste(self):
        actions.key("ctrl-shift-v")

    def copy(self):
        actions.key("ctrl-shift-c")

    def find(text: str = None):
        actions.key("ctrl-shift-f")
        if text:
            actions.insert(text)

    def delete_line(self):
        actions.edit.line_start()
        actions.key("ctrl-k")
