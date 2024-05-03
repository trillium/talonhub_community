from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_assignment", desc="Tag for enabling assignment commands")


@mod.action_class
class Actions:
    def code_operator_assignment(self):
        """code_operator_assignment"""

    def code_or_operator_assignment(self):
        """code_operator_assignment"""

    def code_operator_subtraction_assignment(self):
        """code_operator_subtraction_assignment"""

    def code_operator_addition_assignment(self):
        """code_operator_addition_assignment"""

    def code_operator_increment(self):
        """code_operator_increment"""

    def code_operator_multiplication_assignment(self):
        """code_operator_multiplication_assignment"""

    def code_operator_division_assignment(self):
        """code_operator_division_assignment"""

    def code_operator_modulo_assignment(self):
        """code_operator_modulo_assignment"""

    def code_operator_bitwise_and_assignment(self):
        """code_operator_and_assignment"""

    def code_operator_bitwise_or_assignment(self):
        """code_operator_or_assignment"""

    def code_operator_bitwise_exclusive_or_assignment(self):
        """code_operator_bitwise_exclusive_or_assignment"""

    def code_operator_bitwise_left_shift_assignment(self):
        """code_operator_bitwise_left_shift_assigment"""

    def code_operator_bitwise_right_shift_assignment(self):
        """code_operator_bitwise_right_shift_assignment"""
