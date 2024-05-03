import os
import os.path
import tempfile
import time
from pathlib import Path

import requests
from talon import Context, Module, actions, clip, ui

# Courtesy of https://github.com/anonfunc/talon-user/blob/master/apps/jetbrains.py

extendCommands = []

# Each IDE gets its own port, as otherwise you wouldn't be able
# to run two at the same time and switch between them.
# Note that MPS and IntelliJ ultimate will conflict...
port_mapping = {
    "com.google.android.studio": 8652,
    "com.jetbrains.AppCode": 8655,
    "com.jetbrains.CLion": 8657,
    "com.jetbrains.datagrip": 8664,
    "com.jetbrains.goland-EAP": 8659,
    "com.jetbrains.goland": 8659,
    "com.jetbrains.intellij-EAP": 8653,
    "com.jetbrains.intellij.ce": 8654,
    "com.jetbrains.intellij": 8653,
    "com.jetbrains.PhpStorm": 8662,
    "com.jetbrains.pycharm": 8658,
    "com.jetbrains.rider": 8660,
    "com.jetbrains.rubymine": 8661,
    "com.jetbrains.rubymine-EAP": 8661,
    "com.jetbrains.WebStorm": 8663,
    "google-android-studio": 8652,
    "idea64.exe": 8653,
    "IntelliJ IDEA": 8653,
    "jetbrains-appcode": 8655,
    "jetbrains-clion": 8657,
    "jetbrains-datagrip": 8664,
    "jetbrains-goland-eap": 8659,
    "jetbrains-goland": 8659,
    "jetbrains-idea-ce": 8654,
    "jetbrains-idea-eap": 8653,
    "jetbrains-idea": 8653,
    "jetbrains-phpstorm": 8662,
    "jetbrains-pycharm-ce": 8658,
    "jetbrains-pycharm": 8658,
    "jetbrains-rider": 8660,
    "JetBrains Rider": 8660,
    "jetbrains-rubymine": 8661,
    "jetbrains-rubymine-eap": 8661,
    "jetbrains-studio": 8652,
    "jetbrains-webstorm": 8663,
    "RubyMine": 8661,
    "RubyMine-EAP": 8661,
    "PyCharm": 8658,
    "pycharm64.exe": 8658,
    "WebStorm": 8663,
    "webstorm64.exe": 8663,
}


def _get_nonce(port, file_prefix):
    file_name = file_prefix + str(port)
    try:
        with open(os.path.join(tempfile.gettempdir(), file_name)) as fh:
            return fh.read()
    except FileNotFoundError as e:
        try:
            home = str(Path.home())
            with open(os.path.join(home, file_name)) as fh:
                return fh.read()
        except FileNotFoundError as eb:
            print(f"Could not find {file_name} in tmp or home")
            return None
    except OSError as e:
        print(e)
        return None


def send_idea_command(cmd):
    print(f"Sending {cmd}")
    active_app = ui.active_app()
    bundle = active_app.bundle or active_app.name
    port = port_mapping.get(bundle, None)
    nonce = _get_nonce(port, ".vcidea_") or _get_nonce(port, "vcidea_")
    proxies = {"http": None, "https": None}
    print(f"sending {bundle} {port} {nonce}")
    if port and nonce:
        response = requests.get(
            f"http://localhost:{port}/{nonce}/{cmd}",
            proxies=proxies,
            timeout=(0.05, 3.05),
        )
        response.raise_for_status()
        return response.text


def get_idea_location():
    return send_idea_command("location").split()


def idea_commands(commands):
    command_list = commands.split(",")
    print("executing jetbrains", commands)
    global extendCommands
    extendCommands = command_list
    for cmd in command_list:
        if cmd:
            send_idea_command(cmd.strip())
            time.sleep(0.1)


ctx = Context()
mod = Module()

mod.apps.jetbrains = "app.name: /jetbrains/"
mod.apps.jetbrains = "app.name: CLion"
mod.apps.jetbrains = "app.name: IntelliJ IDEA"
mod.apps.jetbrains = "app.name: PhpStorm"
mod.apps.jetbrains = "app.name: PyCharm"
mod.apps.jetbrains = "app.name: WebStorm"
mod.apps.jetbrains = "app.name: RubyMine"
mod.apps.jetbrains = "app.name: RubyMine-EAP"
mod.apps.jetbrains = "app.name: DataGrip"
mod.apps.jetbrains = """
os: mac
and app.bundle: com.google.android.studio
"""
# windows
mod.apps.jetbrains = "app.exe: idea64.exe"
mod.apps.jetbrains = "app.exe: /^PyCharm64\.exe$/i"
mod.apps.jetbrains = "app.exe: webstorm64.exe"
mod.apps.jetbrains = """
os: mac
and app.bundle: com.jetbrains.pycharm
os: mac
and app.bundle: com.jetbrains.rider
"""
mod.apps.jetbrains = """
os: windows
and app.name: JetBrains Rider
os: windows
and app.exe: rider64.exe
"""


@mod.action_class
class Actions:
    def idea(commands: str):
        """Send a command to Jetbrains product"""
        idea_commands(commands)

    def idea_grab(times: int):
        """Copies specified number of words to the left"""
        old_clip = clip.get()
        try:
            original_line, original_column = get_idea_location()
            for _ in range(times):
                send_idea_command("action EditorSelectWord")
            send_idea_command("action EditorCopy")
            send_idea_command(f"goto {original_line} {original_column}")
            send_idea_command("action EditorPaste")
        finally:
            clip.set(old_clip)
            global extendCommands
            extendCommands = []


ctx.matches = r"""
app: jetbrains
"""


@ctx.action_class("app")
class AppActions:
    def tab_next(self):
        actions.user.idea("action NextTab")

    def tab_previous(self):
        actions.user.idea("action PreviousTab")

    def tab_close(self):
        actions.user.idea("action CloseContent")

    def tab_reopen(self):
        actions.user.idea("action ReopenClosedTab")


@ctx.action_class("code")
class CodeActions:
    # talon code actions
    def toggle_comment(self):
        actions.user.idea("action CommentByLineComment")


@ctx.action_class("edit")
class EditActions:
    # talon edit actions
    def copy(self):
        actions.user.idea("action EditorCopy")

    def cut(self):
        actions.user.idea("action EditorCut")

    def delete(self):
        actions.user.idea("action EditorBackSpace")

    def paste(self):
        actions.user.idea("action EditorPaste")

    def find_next(self):
        actions.user.idea("action FindNext")

    def find_previous(self):
        actions.user.idea("action FindPrevious")

    def find(text: str = None):
        actions.user.idea("action Find")

    def line_clone(self):
        actions.user.idea("action EditorDuplicate")

    def line_swap_down(self):
        actions.user.idea("action MoveLineDown")

    def line_swap_up(self):
        actions.user.idea("action MoveLineUp")

    def indent_more(self):
        actions.user.idea("action EditorIndentLineOrSelection")

    def indent_less(self):
        actions.user.idea("action EditorUnindentSelection")

    def select_line(n: int = None):
        actions.user.idea("action EditorSelectLine")

    def select_word(self):
        actions.user.idea("action EditorSelectWord")

    def select_all(self):
        actions.user.idea("action $SelectAll")

    def file_start(self):
        actions.user.idea("action EditorTextStart")

    def file_end(self):
        actions.user.idea("action EditorTextEnd")

    def extend_file_start(self):
        actions.user.idea("action EditorTextStartWithSelection")

    def extend_file_end(self):
        actions.user.idea("action EditorTextEndWithSelection")

    def extend_word_left(self):
        actions.user.idea("action EditorPreviousWordWithSelection")

    def extend_word_right(self):
        actions.user.idea("action EditorNextWordWithSelection")

    def jump_line(n: int):
        actions.user.idea(f"goto {n} 0")
        # move the cursor to the first nonwhite space character of the line
        actions.user.idea("action EditorLineEnd")
        actions.user.idea("action EditorLineStart")


@ctx.action_class("win")
class WinActions:
    def filename(self) -> str:
        title: str = actions.win.title()
        result = title.split()

        # iterate over reversed result
        # to support titles such as
        # Class.Library2 – a.js [.workspace]
        for word in reversed(result):
            if not word.startswith("[") and "." in word:
                return word

        return ""


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        # depends on plugin GoToTabs
        if number < 10:
            actions.user.idea(f"action GoToTab{number}")

    def extend_until_line(line: int):
        actions.user.idea(f"extend {line}")

    def select_range(line_start: int, line_end: int):
        # if it's a single line, select the entire thing including the ending new-line5
        if line_start == line_end:
            actions.user.idea(f"goto {line_start} 0")
            actions.user.idea("action EditorSelectLine"),
        else:
            actions.user.idea(f"range {line_start} {line_end}")

    def extend_camel_left(self):
        actions.user.idea("action EditorPreviousWordInDifferentHumpsModeWithSelection")

    def extend_camel_right(self):
        actions.user.idea("action EditorNextWordInDifferentHumpsModeWithSelection")

    def camel_left(self):
        actions.user.idea("action EditorPreviousWordInDifferentHumpsMode")

    def camel_right(self):
        actions.user.idea("action EditorNextWordInDifferentHumpsMode")

    def line_clone(line: int):
        actions.user.idea(f"clone {line}")

    # multi-cursor tag functions
    def multi_cursor_enable(self):
        actions.skip()

    def multi_cursor_disable(self):
        actions.key("escape")

    def multi_cursor_add_above(self):
        actions.user.idea("action EditorCloneCaretAbove")

    def multi_cursor_add_below(self):
        actions.user.idea("action EditorCloneCaretBelow")

    def multi_cursor_select_fewer_occurrences(self):
        actions.user.idea("action UnselectPreviousOccurrence")

    def multi_cursor_select_more_occurrences(self):
        actions.user.idea("action SelectNextOccurrence")

    # def multi_cursor_skip_occurrence():
    def multi_cursor_select_all_occurrences(self):
        actions.user.idea("action SelectAllOccurrences")

    def multi_cursor_add_to_line_ends(self):
        actions.user.idea("action EditorAddCaretPerSelectedLine")

    # splits tag functions
    # def split_window_right():
    #     actions.user.idea("action OpenInRightSplit")
    # def split_window_left():
    # def split_window_down():
    # def split_window_up():
    def split_window_vertically(self):
        actions.user.idea("action SplitVertically")

    def split_window_horizontally(self):
        actions.user.idea("action SplitHorizontally")

    def split_flip(self):
        actions.user.idea("action ChangeSplitOrientation")

    def split_maximize(self):
        actions.key("ctrl-shift-f12")

    def split_reset(self):
        actions.key("shift-f12")

    # def split_window():
    def split_clear(self):
        actions.user.idea("action Unsplit")

    def split_clear_all(self):
        actions.user.idea("action UnsplitAll")

    def split_next(self):
        actions.user.idea("action NextSplitter")

    # def split_last():
    # def split_number(index: int):
