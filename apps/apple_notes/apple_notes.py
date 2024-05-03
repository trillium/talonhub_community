from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app: notes
"""


@ctx.action_class("edit")
class EditActions:
    def zoom_in(self):
        actions.key("shift-cmd->")

    def zoom_out(self):
        actions.key("shift-cmd-<")

    def zoom_reset(self):
        actions.key("shift-cmd-0")

    def indent_less(self):
        actions.key("cmd-[")
