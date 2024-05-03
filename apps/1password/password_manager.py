from talon import Module

mod = Module()

# 1password
mod.apps.one_password = "app.bundle: com.agilebits.onepassword7"
mod.apps.one_password = "app.name: 1Password for Windows desktop"
mod.apps.one_password = "app.name: 1Password.exe"


@mod.action_class
class Actions:
    def password_fill(self):
        """fill the password"""

    def password_show(self):
        """show the password"""

    def password_new(self):
        """New password"""

    def password_duplicate(self):
        """Duplicate password"""

    def password_edit(self):
        """Edit password"""

    def password_delete(self):
        """Delete password"""
