from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.calibre_viewer = """
app: calibre
title: /E-book viewer$/
title: /eBook-Betrachter$/
"""

# Context matching
ctx = Context()
ctx.matches = """
os: windows
os: linux
app: calibre_viewer
"""
# TODO: mac implementation


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_next(self):
        actions.key("pagedown")

    def page_previous(self):
        actions.key("pageup")

    def page_final(self):
        actions.key("ctrl-end")

    # user.chapters
    def chapter_next(self):
        actions.key("ctrl-pagedown")

    def chapter_previous(self):
        actions.key("ctrl-pageup")
