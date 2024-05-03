from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: mac
tag: browser
app: firefox
"""


@ctx.action_class("user")
class UserActions:
    def firefox_bookmarks_sidebar(self):
        actions.key("cmd-b")

    def firefox_history_sidebar(self):
        actions.key("cmd-shift-h")


@ctx.action_class("browser")
class BrowserActions:
    def bookmarks(self):
        actions.key("cmd-shift-o")

    def open_private_window(self):
        actions.key("cmd-shift-p")

    def show_downloads(self):
        actions.key("cmd-j")

    def show_extensions(self):
        actions.key("cmd-shift-a")
