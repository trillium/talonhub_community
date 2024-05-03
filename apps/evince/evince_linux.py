from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.evince = """
os: linux
and app.name: Evince
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: evince
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(self):
        actions.key("ctrl-l")
        page = actions.edit.selected_text()
        actions.key("escape")
        return int(page)

    def page_next(self):
        actions.key("n")

    def page_previous(self):
        actions.key("p")

    def page_jump(number: int):
        actions.key("ctrl-l")
        actions.insert(str(number))
        actions.key("enter")

    def page_final(self):
        actions.key("ctrl-end")
