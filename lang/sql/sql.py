from talon import Context, actions

ctx = Context()
ctx.matches = r"""
code.language: sql
"""

# these vary by dialect
ctx.lists["user.code_common_function"] = {"count": "Count", "min": "Min", "max": "Max"}


@ctx.action_class("user")
class UserActions:
    def code_operator_addition(self):
        actions.auto_insert(" + ")

    def code_operator_subtraction(self):
        actions.auto_insert(" - ")

    def code_operator_multiplication(self):
        actions.auto_insert(" * ")

    def code_operator_division(self):
        actions.auto_insert(" / ")

    def code_operator_equal(self):
        actions.auto_insert(" = ")

    def code_operator_not_equal(self):
        actions.auto_insert(" <> ")

    def code_operator_greater_than(self):
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to(self):
        actions.auto_insert(" >= ")

    def code_operator_less_than(self):
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to(self):
        actions.auto_insert(" <= ")

    def code_operator_in(self):
        actions.user.insert_between(" IN (", ")")

    def code_operator_not_in(self):
        actions.user.insert_between(" NOT IN (", ")")

    def code_operator_and(self):
        actions.auto_insert("AND ")

    def code_operator_or(self):
        actions.auto_insert("OR ")

    def code_insert_null(self):
        actions.auto_insert("NULL")

    def code_insert_is_null(self):
        actions.auto_insert(" IS NULL")

    def code_insert_is_not_null(self):
        actions.auto_insert(" IS NOT NULL")

    def code_comment_line_prefix(self):
        actions.auto_insert("-- ")

    def code_insert_function(text: str, selection: str):
        actions.user.insert_between(f"{text}({selection or ''}", ")")
