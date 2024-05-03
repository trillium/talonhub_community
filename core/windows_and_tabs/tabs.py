from talon import Module, actions, app

mod = Module()


@mod.action_class
class tab_actions:
    def tab_jump(number: int):
        """Jumps to the specified tab"""

    def tab_final(self):
        """Jumps to the final tab"""

    def tab_close_wrapper(self):
        """Closes the current tab.
        Exists so that apps can implement their own delay before running tab_close() to handle repetitions better.
        """
        actions.app.tab_close()

    def tab_duplicate(self):
        """Duplicates the current tab."""
