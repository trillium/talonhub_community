from talon import Context, Module, actions

# App definition
mod = Module()
mod.apps.gnome_terminal = """
os: linux
and app.exe: gnome-terminal-server
os: linux
and app.name: Gnome-terminal
os: linux
and app.name: Mate-terminal
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: gnome_terminal
"""


# --- Implement actions ---
@ctx.action_class("user")
class user_actions:
    # user.tabs
    def tab_jump(number):
        actions.key(f"alt-{number}")


@ctx.action_class("app")
class app_actions:
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
        actions.key("ctrl-shift-n")

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

    # afaik not possible in gnome-terminal
    def extend_left(self):
        pass

    def extend_right(self):
        pass

    def extend_up(self):
        pass

    def extend_down(self):
        pass

    def extend_word_left(self):
        pass

    def extend_word_right(self):
        pass
