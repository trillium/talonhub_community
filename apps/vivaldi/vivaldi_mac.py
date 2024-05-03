from talon import Context, actions, app

ctx = Context()

ctx.matches = r"""
os: mac
app: vivaldi
"""


@ctx.action_class("user")
class UserActions:
    def vivaldi_history_panel(self):
        actions.key("cmd-alt-y")

    def vivaldi_downloads_panel(self):
        actions.key("cmd-alt-l")

    def vivaldi_notes_panel(self):
        # This shortcut didn't work for me. You might need to change it to a
        # different one.
        actions.key("cmd-alt-n")

    def vivaldi_toggle_quick_commands(self):
        actions.key("cmd-e")

    def tab_jump(number: int):
        actions.key(f"cmd-{number}")


@ctx.action_class("app")
class AppActions:
    def tab_next(self):
        actions.key("cmd-shift-]")

    def tab_previous(self):
        actions.key("cmd-shift-[")


@ctx.action_class("browser")
class BrowserActions:
    def show_extensions(self):
        actions.key("ctrl-cmd-e")

    def bookmarks(self):
        actions.key("cmd-ctrl-b")

    def focus_address(self):
        actions.key("cmd-l")
