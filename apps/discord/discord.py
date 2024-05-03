from talon import Context, Module, actions

mod = Module()
apps = mod.apps
apps.discord = "app.bundle: com.hnc.Discord"
apps.discord = "app.name: Discord"
apps.discord = "app.name: Discord.exe"
apps.discord = """
tag: browser
browser.host: discord.com
"""

mod.list("discord_destination", desc="discord destination")

ctx = Context()
ctx.matches = r"""
app: discord
"""

ctx.lists["user.discord_destination"] = {
    "user": "@",
    "voice": "!",
    "server": "*",
}


@mod.action_class
class discord_actions:
    def discord_mentions_last(self):
        """Go up to channel with unread mentions"""

    def discord_mentions_next(self):
        """Go down to channel with unread mentions"""

    def discord_oldest_unread(self):
        """Go to oldest unread message"""

    def discord_toggle_pins(self):
        """Toggle pins popout"""

    def discord_toggle_inbox(self):
        """Toggle inbox popout"""

    def discord_toggle_members(self):
        """Toggle channel member list"""

    def discord_emoji_picker(self):
        """Toggle emoji picker"""

    def discord_gif_picker(self):
        """Toggle gif picker"""

    def discord_sticker_picker(self):
        """Toggle sticker picker"""

    def discord_mark_inbox_read(self):
        """Mark top inbox channel read"""

    def discord_mute(self):
        """Toggle mute"""

    def discord_deafen(self):
        """Toggle deafen"""

    def discord_answer_call(self):
        """Answer incoming call"""

    def discord_decline_call(self):
        """Decline incoming call"""

    def discord_quick_switcher(dest_type: str, dest_search: str):
        """Open up the quick switcher, optionally specifying a type of destination"""

    def discord_go_current_call(self):
        """Go to current call"""

    def discord_toggle_dms(self):
        """Toggle between dms and your most recent server"""


@ctx.action_class("user")
class UserActions:
    # Navigation: Channels
    def messaging_open_channel_picker(self):
        actions.user.discord_quick_switcher("#", "")
