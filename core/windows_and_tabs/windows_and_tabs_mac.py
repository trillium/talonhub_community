from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class AppActions:
    def preferences(self):
        actions.key("cmd-,")

    def tab_close(self):
        actions.key("cmd-w")

    def tab_next(self):
        actions.key("ctrl-tab")

    def tab_open(self):
        actions.key("cmd-t")

    def tab_previous(self):
        actions.key("ctrl-shift-tab")

    def tab_reopen(self):
        actions.key("cmd-shift-t")

    def window_close(self):
        actions.key("cmd-w")

    def window_hide(self):
        actions.key("cmd-m")

    def window_hide_others(self):
        actions.key("cmd-alt-h")

    def window_open(self):
        actions.key("cmd-n")

    def window_previous(self):
        actions.key("cmd-shift-`")

    def window_next(self):
        actions.key("cmd-`")


@ctx.action_class("user")
class UserActions:
    def switcher_focus_last(self):
        actions.key("cmd-tab")
