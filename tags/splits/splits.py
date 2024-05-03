from talon import Module

mod = Module()
mod.tag("splits", desc="Tag for enabling generic window split commands")


@mod.action_class
class Actions:
    def split_window_right(self):
        """Move active tab to right split"""

    def split_window_left(self):
        """Move active tab to left split"""

    def split_window_down(self):
        """Move active tab to lower split"""

    def split_window_up(self):
        """Move active tab to upper split"""

    def split_window_vertically(self):
        """Splits window vertically"""

    def split_window_horizontally(self):
        """Splits window horizontally"""

    def split_flip(self):
        """Flips the orietation of the active split"""

    def split_maximize(self):
        """Maximizes the active split"""

    def split_reset(self):
        """Resets the split sizes"""

    def split_window(self):
        """Splits the window"""

    def split_clear(self):
        """Clears the current split"""

    def split_clear_all(self):
        """Clears all splits"""

    def split_next(self):
        """Goes to next split"""

    def split_last(self):
        """Goes to last split"""

    def split_number(index: int):
        """Navigates to a the specified split"""
