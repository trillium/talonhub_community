from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
app: slack
"""


@ctx.action_class("user")
class UserActions:
    def messaging_workspace_previous(self):
        actions.key("cmd-shift-[")

    def messaging_workspace_next(self):
        actions.key("cmd-shift-]")

    def messaging_open_channel_picker(self):
        actions.key("cmd-k")

    def messaging_channel_previous(self):
        actions.key("alt-up")

    def messaging_channel_next(self):
        actions.key("alt-down")

    def messaging_unread_previous(self):
        actions.key("alt-shift-up")

    def messaging_unread_next(self):
        actions.key("alt-shift-down")

    def messaging_open_search(self):
        actions.key("cmd-f")

    def messaging_mark_workspace_read(self):
        actions.key("shift-esc")

    def messaging_mark_channel_read(self):
        actions.key("esc")

    # Files and Snippets
    def messaging_upload_file(self):
        actions.key("cmd-u")
