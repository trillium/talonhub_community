# defines the default app actions for windows

from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("app")
class AppActions:
    # app.preferences()

    def tab_close(self):
        actions.key("ctrl-w")

    def tab_next(self):
        actions.key("ctrl-tab")

    def tab_open(self):
        actions.key("ctrl-t")

    def tab_previous(self):
        actions.key("ctrl-shift-tab")

    def tab_reopen(self):
        actions.key("ctrl-shift-t")

    def window_close(self):
        actions.key("alt-f4")

    def window_hide(self):
        actions.key("alt-space n")

    def window_hide_others(self):
        actions.key("win-d alt-tab")

    def window_open(self):
        actions.key("ctrl-n")


@ctx.action_class("user")
class UserActions:
    def switcher_focus_last(self):
        actions.key("alt-tab")
