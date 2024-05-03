from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
code.language: ruby
"""


@ctx.action_class("user")
class UserActions:
    def code_operator_lambda(self):
        actions.auto_insert("->")

    def code_operator_subscript(self):
        actions.insert("[]")
        actions.key("left")

    def code_operator_assignment(self):
        actions.auto_insert(" = ")

    def code_or_operator_assignment(self):
        actions.auto_insert(" ||= ")

    def code_operator_subtraction(self):
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment(self):
        actions.auto_insert(" -= ")

    def code_operator_addition(self):
        actions.auto_insert(" + ")

    def code_operator_addition_assignment(self):
        actions.auto_insert(" += ")

    def code_operator_multiplication(self):
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment(self):
        actions.auto_insert(" *= ")

    def code_operator_exponent(self):
        actions.auto_insert(" ** ")

    def code_operator_division(self):
        actions.auto_insert(" / ")

    def code_operator_division_assignment(self):
        actions.auto_insert(" /= ")

    def code_operator_modulo(self):
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment(self):
        actions.auto_insert(" %= ")

    def code_operator_equal(self):
        actions.auto_insert(" == ")

    def code_operator_not_equal(self):
        actions.auto_insert(" != ")

    def code_operator_greater_than(self):
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to(self):
        actions.auto_insert(" >= ")

    def code_operator_less_than(self):
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to(self):
        actions.auto_insert(" <= ")

    def code_operator_and(self):
        actions.auto_insert(" && ")

    def code_operator_or(self):
        actions.auto_insert(" || ")

    def code_operator_bitwise_and(self):
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment(self):
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or(self):
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment(self):
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or(self):
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment(self):
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift(self):
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment(self):
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift(self):
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment(self):
        actions.auto_insert(" >>= ")

    def code_self(self):
        actions.auto_insert("self")

    def code_operator_object_accessor(self):
        actions.auto_insert(".")

    def code_insert_null(self):
        actions.auto_insert("nil")

    def code_insert_is_null(self):
        actions.auto_insert(".nil?")

    # Technically .present? is provided by Rails
    def code_insert_is_not_null(self):
        actions.auto_insert(".present?")

    def code_state_do(self):
        actions.insert("do ")

    def code_state_if(self):
        actions.insert("if ")

    def code_state_else_if(self):
        actions.insert("elsif ")

    def code_state_else(self):
        actions.insert("else")
        actions.key("enter")

    def code_state_switch(self):
        actions.insert("case ")

    def code_state_case(self):
        actions.insert("when ")

    def code_state_for_each(self):
        actions.insert(".each do ||")
        actions.key("left")

    def code_define_class(self):
        actions.auto_insert("class ")

    def code_import(self):
        actions.auto_insert('require ""')
        actions.key("left")

    def code_comment_line_prefix(self):
        actions.auto_insert("# ")

    def code_state_return(self):
        actions.insert("return ")

    def code_insert_true(self):
        actions.auto_insert("true")

    def code_insert_false(self):
        actions.auto_insert("false")

    def code_comment_documentation(self):
        actions.insert("##")
        actions.key("enter")
        actions.key("space")
        ### Extra non-standard things

    def code_default_function(text: str):
        """Inserts function definition"""

        result = "def {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
