from talon import Context, actions

ctx = Context()

# i don't see a need to restrict the app here, this just defines the actions
# each app can support appropriate voice commands as needed
# the below are for 1password, redefine as needed
ctx.matches = r"""
os: windows
"""


@ctx.action_class("user")
class UserActions:
    def password_fill(self):
        actions.key("ctrl-\\\\")

    def password_show(self):
        actions.key("alt-ctrl-\\\\")

    def password_new(self):
        actions.key("ctrl-n")

    def password_duplicate(self):
        actions.key("ctrl-d")

    def password_edit(self):
        actions.key("ctrl-e")

    def password_delete(self):
        actions.key("ctrl-delete")
