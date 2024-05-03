from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: vimscript
"""

ctx.lists["self.vimscript_functions"] = {
    "string len": "strlen",
    "get line": "getline",
    "set line": "setline",
    "length": "len",
}

ctx.lists["self.vimscript_scope"] = {
    "argument": "a:",
    "arg": "a:",
    "buffer": "b:",
    "buf": "b:",
    "window": "w:",
    "win": "w:",
    "tab": "t:",
    "special": "v:",
    "global": "g:",
    "local": "l:",
    "script local": "s:",
}

mod.list("vimscript_functions", desc="Standard built-in vimscript functions")
mod.list("vimscript_scope", desc="vimscript scoping types for functions and variables")


@mod.capture(rule="{self.vimscript_functions}")
def vimscript_functions(m) -> str:
    "Returns a string"
    return m.vimscript_functions


@mod.capture(rule="{self.vimscript_scope}")
def vimscript_scope(m) -> str:
    "Returns a string"
    return m.vimscript_scope


@ctx.action_class("user")
class UserActions:
    def code_operator_assignment(self):
        actions.auto_insert(" = ")

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

    def code_operator_division(self):
        actions.auto_insert(" / ")

    def code_operator_division_assignment(self):
        actions.auto_insert(" /= ")

    def code_comment_line_prefix(self):
        actions.auto_insert('"')

    def code_state_if(self):
        actions.insert("if ")

    def code_state_else_if(self):
        actions.insert("elseif ")

    def code_state_else(self):
        actions.insert("else")

    def code_private_function(text: str):
        actions.auto_insert("function ")

    def code_protected_function(text: str):
        actions.auto_insert("function ")

    def code_public_function(text: str):
        actions.auto_insert("function ")
