from talon import Module

mod = Module()


@mod.action_class
class Actions:
    def terminal_list_directories(self):
        """Lists directories"""

    def terminal_list_all_directories(self):
        """Lists all directories including hidden"""

    def terminal_change_directory(path: str):
        """Lists change directory"""

    def terminal_change_directory_root(self):
        """Root of current drive"""

    def terminal_clear_screen(self):
        """Clear screen"""

    def terminal_run_last(self):
        """Repeats the last command"""

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    def terminal_kill_all(self):
        """kills the running command"""
