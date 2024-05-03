from talon import Module

mod = Module()
mod.tag("messaging", desc="Tag for generic multi-channel messaging apps")


@mod.action_class
class messaging_actions:
    # Navigation and UI components

    def messaging_workspace_previous(self):
        """Move to previous workspace/server"""

    def messaging_workspace_next(self):
        """Move to next qorkspace/server"""

    def messaging_open_channel_picker(self):
        """Open channel picker"""

    def messaging_channel_previous(self):
        """Move to previous channel"""

    def messaging_channel_next(self):
        """Move to next channel"""

    def messaging_unread_previous(self):
        """Move to previous unread channel"""

    def messaging_unread_next(self):
        """Moved to next unread channel"""

    def messaging_open_search(self):
        """Open message search"""

    def messaging_mark_workspace_read(self):
        """Mark this workspace/server as read"""

    def messaging_mark_channel_read(self):
        """Mark this channel as read."""

    def messaging_upload_file(self):
        """Upload a file as a message"""
