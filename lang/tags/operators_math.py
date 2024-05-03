from talon import Context, Module

ctx = Context()
mod = Module()


# TODO: Could split into numeric, comparison, and logic?

mod.tag("code_operators_math", desc="Tag for enabling mathematical operator commands")


@mod.action_class
class Actions:
    def code_operator_subtraction(self):
        """code_operator_subtraction"""

    def code_operator_addition(self):
        """code_operator_addition"""

    def code_operator_multiplication(self):
        """code_operator_multiplication"""

    def code_operator_exponent(self):
        """code_operator_exponent"""

    def code_operator_division(self):
        """code_operator_division"""

    def code_operator_modulo(self):
        """code_operator_modulo"""

    def code_operator_equal(self):
        """code_operator_equal"""

    def code_operator_not_equal(self):
        """code_operator_not_equal"""

    def code_operator_greater_than(self):
        """code_operator_greater_than"""

    def code_operator_greater_than_or_equal_to(self):
        """code_operator_greater_than_or_equal_to"""

    def code_operator_less_than(self):
        """code_operator_less_than"""

    def code_operator_less_than_or_equal_to(self):
        """code_operator_less_than_or_equal_to"""

    def code_operator_and(self):
        """code_operator_and"""

    def code_operator_or(self):
        """code_operator_or"""

    def code_operator_in(self):
        """code_operator_in"""

    def code_operator_not_in(self):
        """code_operator_not_in"""
