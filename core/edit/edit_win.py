# defines the default edit actions for windows

from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("edit")
class EditActions:
    def copy(self):
        actions.key("ctrl-c")

    def cut(self):
        actions.key("ctrl-x")

    def delete(self):
        actions.key("backspace")

    def delete_line(self):
        actions.edit.select_line()
        actions.edit.delete()
        # action(edit.delete_paragraph):
        # action(edit.delete_sentence):

    def delete_word(self):
        actions.edit.select_word()
        actions.edit.delete()

    def down(self):
        actions.key("down")
        # action(edit.extend_again):
        # action(edit.extend_column):

    def extend_down(self):
        actions.key("shift-down")

    def extend_file_end(self):
        actions.key("shift-ctrl-end")

    def extend_file_start(self):
        actions.key("shift-ctrl-home")

    def extend_left(self):
        actions.key("shift-left")
        # action(edit.extend_line):

    def extend_line_down(self):
        actions.key("shift-down")

    def extend_line_end(self):
        actions.key("shift-end")

    def extend_line_start(self):
        actions.key("shift-home")

    def extend_line_up(self):
        actions.key("shift-up")

    def extend_page_down(self):
        actions.key("shift-pagedown")

    def extend_page_up(self):
        actions.key("shift-pageup")
        # action(edit.extend_paragraph_end):
        # action(edit.extend_paragraph_next()):
        # action(edit.extend_paragraph_previous()):
        # action(edit.extend_paragraph_start()):

    def extend_right(self):
        actions.key("shift-right")
        # action(edit.extend_sentence_end):
        # action(edit.extend_sentence_next):
        # action(edit.extend_sentence_previous):
        # action(edit.extend_sentence_start):

    def extend_up(self):
        actions.key("shift-up")

    def extend_word_left(self):
        actions.key("ctrl-shift-left")

    def extend_word_right(self):
        actions.key("ctrl-shift-right")

    def file_end(self):
        actions.key("ctrl-end")

    def file_start(self):
        actions.key("ctrl-home")

    def find(text: str = ""):
        actions.key("ctrl-f")
        actions.insert(text)

    def find_next(self):
        actions.key("f3")
        # action(edit.find_previous):

    def indent_less(self):
        actions.key("home delete")

    def indent_more(self):
        actions.key("home tab")
        # action(edit.jump_column(n: int)
        # action(edit.jump_line(n: int)

    def left(self):
        actions.key("left")

    def line_down(self):
        actions.key("down home")

    def line_end(self):
        actions.key("end")

    def line_insert_up(self):
        actions.key("home enter up")

    def line_start(self):
        actions.key("home")

    def line_up(self):
        actions.key("up home")
        # action(edit.move_again):

    def page_down(self):
        actions.key("pagedown")

    def page_up(self):
        actions.key("pageup")
        # action(edit.paragraph_end):
        # action(edit.paragraph_next):
        # action(edit.paragraph_previous):
        # action(edit.paragraph_start):

    def paste(self):
        actions.key("ctrl-v")
        # action(paste_match_style):

    def print(self):
        actions.key("ctrl-p")

    def redo(self):
        actions.key("ctrl-y")

    def right(self):
        actions.key("right")

    def save(self):
        actions.key("ctrl-s")

    def save_all(self):
        actions.key("ctrl-shift-s")

    def select_all(self):
        actions.key("ctrl-a")

    def select_line(n: int = None):
        if n is not None:
            actions.edit.jump_line(n)
        actions.key("end shift-home")
        # action(edit.select_lines(a: int, b: int)):

    def select_none(self):
        actions.key("right")
        # action(edit.select_paragraph):
        # action(edit.select_sentence):

    def undo(self):
        actions.key("ctrl-z")

    def up(self):
        actions.key("up")

    def word_left(self):
        actions.key("ctrl-left")

    def word_right(self):
        actions.key("ctrl-right")

    def zoom_in(self):
        actions.key("ctrl-+")

    def zoom_out(self):
        actions.key("ctrl--")

    def zoom_reset(self):
        actions.key("ctrl-0")
