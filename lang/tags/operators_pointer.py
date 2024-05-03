from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_pointer", desc="Tag for enabling pointer operator commands")


@mod.action_class
class Actions:
    def code_operator_indirection(self):
        """code_operator_indirection"""

    def code_operator_address_of(self):
        """code_operator_address_of (e.g., C++ & op)"""

    def code_operator_structure_dereference(self):
        """code_operator_structure_dereference (e.g., C++ -> op)"""
