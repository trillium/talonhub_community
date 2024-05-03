from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

mod.apps.vivaldi = "app.name: Vivaldi"
mod.apps.vivaldi = "app.name: Vivaldi-stable"
mod.apps.vivaldi = """
os: windows
and app.exe: vivaldi.exe
os: linux
and app.exe: vivaldi-bin
os: mac
and app.bundle: com.vivaldi.Vivaldi
"""
ctx.matches = r"""
app: vivaldi
"""


@mod.action_class
class Actions:
    def vivaldi_history_panel(self):
        """Toggles the Vivaldi history panel"""
        actions.key("ctrl-shift-h")

    def vivaldi_bookmarks_panel(self):
        """Toggles the Vivaldi bookmarks panel"""
        actions.user.vivaldi_toggle_quick_commands()
        actions.sleep("180ms")
        actions.insert("Bookmarks Panel")
        actions.key("enter")

    def vivaldi_downloads_panel(self):
        """Toggles the Vivaldi downloads panel"""
        actions.key("ctrl-shift-d")

    def vivaldi_notes_panel(self):
        """Toggles the Vivaldi notes panel"""
        actions.key("ctrl-shift-o")

    def vivaldi_toggle_quick_commands(self):
        """Toggles the Vivaldi Quick Commands tool"""
        actions.key("ctrl-e")


@ctx.action_class("user")
class UserActions:
    def tab_close_wrapper(self):
        actions.sleep("180ms")
        actions.app.tab_close()

    def tab_jump(number: int):
        actions.key(f"ctrl-{number}")


@ctx.action_class("browser")
class BrowserActions:
    def show_extensions(self):
        actions.key("ctrl-shift-e")

    def focus_address(self):
        actions.key("ctrl-l")

    def focus_page(self):
        actions.key("f9")

    def bookmarks(self):
        actions.key("ctrl-b")

    def bookmark_tabs(self):
        raise NotImplementedError("Vivaldi doesn't support this functionality")

    def show_downloads(self):
        # There is no default shortcut for showing the downloads page. You can
        # configure one.
        actions.app.tab_open()
        actions.sleep("180ms")
        actions.browser.go("vivaldi://downloads")

    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("150ms")
        actions.insert(url)
        actions.key("enter")
