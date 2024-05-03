from talon import Module

mod = Module()
mod.tag("multiple_cursors", desc="Tag for enabling generic multiple cursor commands")


@mod.action_class
class multiple_cursor_actions:
    def multi_cursor_enable(self):
        """Enables multi-cursor mode"""

    def multi_cursor_disable(self):
        """Disables multi-cursor mode"""

    def multi_cursor_add_above(self):
        """Adds cursor to line above"""

    def multi_cursor_add_below(self):
        """Adds cursor to line below"""

    def multi_cursor_select_fewer_occurrences(self):
        """Removes selection & cursor at last occurrence"""

    def multi_cursor_select_more_occurrences(self):
        """Adds cursor at next occurrence of selection"""

    def multi_cursor_skip_occurrence(self):
        """Skips adding a cursor at next occurrence of selection"""

    def multi_cursor_select_all_occurrences(self):
        """Adds cursor at every occurrence of selection"""

    def multi_cursor_add_to_line_ends(self):
        """Adds cursor at end of every selected line"""
