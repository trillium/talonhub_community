from talon import Context, Module, actions

mod = Module()
ctx = Context()

apps = mod.apps
apps.notepad_plus_plus = """
os: windows
and app.name: Notepad++ : a free (GNU) source code editor
os: windows
and app.name: Notepad++ : a free (GPL) source code editor
os: windows
and app.exe: notepad++.exe
"""

ctx.matches = r"""
app: notepad_plus_plus
"""

ctx.tags = ["user.find_and_replace", "user.line_commands", "user.tabs"]


@ctx.action_class("app")
class AppActions:
    def tab_previous(self):
        actions.key("ctrl-pageup")

    def tab_next(self):
        actions.key("ctrl-pagedown")


@ctx.action_class("code")
class CodeActions:
    def toggle_comment(self):
        actions.key("ctrl-q")


@ctx.action_class("edit")
class EditActions:
    def line_clone(self):
        actions.key("ctrl-d")

    def line_swap_up(self):
        actions.key("ctrl-shift-up")

    def line_swap_down(self):
        actions.key("ctrl-shift-down")

    def indent_more(self):
        actions.key("tab")

    def indent_less(self):
        actions.key("shift-tab")

    def jump_line(n: int):
        actions.key("ctrl-g")
        actions.insert(str(n))
        actions.key("enter")

    def find(text: str):
        actions.key("ctrl-f")
        actions.insert(text)


@ctx.action_class("win")
class win_actions:
    def filename(self):
        title = actions.win.title()
        result = title.split(" - ")[0]
        if "." in result:
            # print(result.split("\\")[-1])
            return result.split("\\")[-1]
        return ""


@ctx.action_class("user")
class UserActions:
    def select_next_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("enter esc")
        actions.sleep("100ms")

    def select_previous_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("shift-enter esc")
        actions.sleep("100ms")

    def tab_jump(number: int):
        if number < 10:
            actions.key(f"ctrl-keypad_{number}")

    def tab_final(self):
        """Jumps to the final tab"""
        print("Notepad doesn't support this...")
        # actions.key("ctrl-numpad_0")

    # find_and_replace.py support begin

    def find(text: str):
        """Triggers find in current editor"""
        actions.key("ctrl-f")

        if text:
            actions.insert(text)

    def find_next(self):
        actions.key("enter")

    def find_previous(self):
        actions.key("shift-enter")

    def find_everywhere(text: str):
        """Triggers find across project"""

        actions.key("ctrl-shift-f")

        if text:
            actions.insert(text)

    def find_toggle_match_by_case(self):
        """Toggles find match by case sensitivity"""
        actions.key("alt-c")

    def find_toggle_match_by_word(self):
        """Toggles find match by whole words"""
        actions.key("alt-w")

    def find_toggle_match_by_regex(self):
        """Toggles find match by regex"""
        actions.key("alt-g")

    def replace(text: str):
        """Search and replaces in the active editor"""
        actions.key("esc ctrl-h")

        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        actions.key("esc ctrl-shift-f")

        if text:
            actions.insert(text)

    def replace_confirm(self):
        """Confirm replace at current position"""
        actions.key("alt-r")

    def replace_confirm_all(self):
        """Confirm replace all"""
        actions.key("alt-a")

    # find_and_replace.py support end
