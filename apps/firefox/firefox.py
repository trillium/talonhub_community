from talon import Context, Module, actions, app

ctx = Context()
mod = Module()
apps = mod.apps
apps.firefox = "app.name: Firefox"
apps.firefox = "app.name: Firefox Developer Edition"
apps.firefox = "app.name: firefox"
apps.firefox = "app.name: Firefox-esr"
apps.firefox = "app.name: LibreWolf"
apps.firefox = "app.name: waterfox"
apps.firefox = """
os: windows
and app.name: Firefox
os: windows
and app.exe: firefox.exe
"""
apps.firefox = """
os: mac
and app.bundle: org.mozilla.firefox
"""

# Make the context match more specifically than anything else. This is important, eg. to
# override the browser.go_home() implementation in tags/browser/browser_mac.py.
ctx.matches = r"""
os: windows
os: linux
os: mac
tag: browser
app: firefox
"""


@mod.action_class
class Actions:
    def firefox_bookmarks_sidebar(self):
        """Toggles the Firefox bookmark sidebar"""

    def firefox_history_sidebar(self):
        """Toggles the Firefox history sidebar"""


@ctx.action_class("user")
class UserActions:
    def tab_close_wrapper(self):
        actions.sleep("180ms")
        actions.app.tab_close()


@ctx.action_class("browser")
class BrowserActions:
    def focus_page(self):
        actions.browser.focus_address()
        actions.edit.find()
        actions.sleep("180ms")
        actions.key("escape")

    def go_home(self):
        actions.key("alt-home")
