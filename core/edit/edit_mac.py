from talon import Context, actions, clip

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("edit")
class EditActions:
    def copy(self):
        actions.key("cmd-c")

    def cut(self):
        actions.key("cmd-x")

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
        actions.key("cmd-shift-down")

    def extend_file_start(self):
        actions.key("cmd-shift-up")

    def extend_left(self):
        actions.key("shift-left")
        # action(edit.extend_line):

    def extend_line_down(self):
        actions.key("shift-down")

    def extend_line_end(self):
        actions.key("cmd-shift-right")

    def extend_line_start(self):
        actions.key("cmd-shift-left")

    def extend_line_up(self):
        actions.key("shift-up")

    def extend_page_down(self):
        actions.key("cmd-shift-pagedown")

    def extend_page_up(self):
        actions.key("cmd-shift-pageup")
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
        actions.key("shift-alt-left")

    def extend_word_right(self):
        actions.key("shift-alt-right")

    def file_end(self):
        actions.key("cmd-down")

    def file_start(self):
        actions.key("cmd-up")

    def find(text: str = None):
        if text is not None:
            clip.set_text(text, mode="find")
        actions.key("cmd-f")

    def find_next(self):
        actions.key("cmd-g")

    def find_previous(self):
        actions.key("cmd-shift-g")

    def indent_less(self):
        actions.key("cmd-left delete")

    def indent_more(self):
        actions.key("cmd-left tab")
        # action(edit.jump_column(n: int)
        # action(edit.jump_line(n: int)

    def left(self):
        actions.key("left")

    def line_down(self):
        actions.key("down home")

    def line_end(self):
        actions.key("cmd-right")

    def line_insert_up(self):
        actions.key("cmd-left enter up")

    def line_start(self):
        actions.key("cmd-left")

    def line_up(self):
        actions.key("up cmd-left")
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
        actions.key("cmd-v")

    def paste_match_style(self):
        actions.key("cmd-alt-shift-v")

    def print(self):
        actions.key("cmd-p")

    def redo(self):
        actions.key("cmd-shift-z")

    def right(self):
        actions.key("right")

    def save(self):
        actions.key("cmd-s")

    def save_all(self):
        actions.key("cmd-alt-s")

    def select_all(self):
        actions.key("cmd-a")

    def select_line(n: int = None):
        if n is not None:
            actions.edit.jump_line(n)
        actions.key("cmd-right cmd-shift-left")
        # action(edit.select_lines(a: int, b: int)):

    def select_none(self):
        actions.key("right")
        # action(edit.select_paragraph):
        # action(edit.select_sentence):

    def undo(self):
        actions.key("cmd-z")

    def up(self):
        actions.key("up")

    def word_left(self):
        actions.key("alt-left")

    def word_right(self):
        actions.key("alt-right")

    def zoom_in(self):
        actions.key("cmd-=")

    def zoom_out(self):
        actions.key("cmd--")

    def zoom_reset(self):
        actions.key("cmd-0")
