from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: visual_studio
"""


@ctx.action_class("app")
class AppActions:
    # talon app actions
    def tab_close(self):
        actions.key("ctrl-f4")

    def tab_next(self):
        actions.key("ctrl-tab")

    def tab_previous(self):
        actions.key("ctrl-shift-tab")

    def tab_reopen(self):
        actions.key("ctrl-1 ctrl-r enter")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment(self):
        actions.key("ctrl-k ctrl-/")


@ctx.action_class("edit")
class EditActions:
    # talon edit actions
    def indent_more(self):
        actions.key("tab")

    def indent_less(self):
        actions.key("shift-tab")

    def save_all(self):
        actions.key("ctrl-shift-s")


@ctx.action_class("user")
class UserActions:
    # multiple_cursor.py support begin
    # note: visual studio has no explicit mode for multiple cursors; requires https://marketplace.visualstudio.com/items?itemName=VaclavNadrasky.MultiCaretBooster
    def multi_cursor_add_above(self):
        actions.key("shift-alt-up")

    def multi_cursor_add_below(self):
        actions.key("shift-alt-down")

    # action(user.multi_cursor_add_to_line_ends): does not exist :(
    def multi_cursor_disable(self):
        actions.key("escape")

    def multi_cursor_enable(self):
        actions.skip()

    def multi_cursor_select_all_occurrences(self):
        actions.key("shift-alt-;")

    def multi_cursor_select_fewer_occurrences(self):
        actions.key("shift-alt-k")

    def multi_cursor_select_more_occurrences(self):
        actions.key("shift-alt->")
