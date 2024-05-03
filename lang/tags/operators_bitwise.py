from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_bitwise", desc="Tag for enabling bitwise operator commands")


@mod.action_class
class Actions:
    def code_operator_bitwise_and(self):
        """code_operator_bitwise_and"""

    def code_operator_bitwise_or(self):
        """code_operator_bitwise_or"""

    def code_operator_bitwise_exclusive_or(self):
        """code_operator_bitwise_exclusive_or"""

    def code_operator_bitwise_left_shift(self):
        """code_operator_bitwise_left_shift"""

    def code_operator_bitwise_right_shift(self):
        """code_operator_bitwise_right_shift"""
