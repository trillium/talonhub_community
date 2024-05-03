from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
code.language: php
"""

ctx.lists["user.code_type"] = {
    "int": "int",
    "float": "float",
    "string": "string",
    "bool": "bool",
    "array": "array",
    "null": "null",
    "void": "void",
}


@ctx.action_class("user")
class UserActions:
    def code_self(self):
        actions.auto_insert("$this")

    def code_operator_object_accessor(self):
        actions.auto_insert("->")

    def code_define_class(self):
        actions.auto_insert("class ")

    def code_import(self):
        actions.auto_insert("use ;")
        actions.edit.left()

    def code_comment_line_prefix(self):
        actions.auto_insert("// ")

    def code_comment_block(self):
        actions.user.code_comment_block_prefix()
        actions.key("enter")
        actions.key("enter")
        actions.user.code_comment_block_suffix()
        actions.edit.up()

    def code_comment_block_prefix(self):
        actions.auto_insert("/*")

    def code_comment_block_suffix(self):
        actions.auto_insert("*/")

    def code_comment_documentation(self):
        actions.insert("/**")

    def code_insert_true(self):
        actions.auto_insert("true")

    def code_insert_false(self):
        actions.auto_insert("false")

    def code_insert_null(self):
        actions.auto_insert("null")

    def code_insert_is_null(self):
        actions.auto_insert("is_null()")
        actions.edit.left()

    def code_insert_is_not_null(self):
        actions.auto_insert("isset()")
        actions.edit.left()

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
        actions.auto_insert(" === ")

    def code_operator_not_equal(self):
        actions.auto_insert(" !== ")

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

    def code_state_if(self):
        actions.insert("if ()")
        actions.edit.left()

    def code_state_else_if(self):
        actions.insert("elseif ()")
        actions.edit.left()

    def code_state_else(self):
        actions.insert("else {")
        actions.key("enter")

    def code_state_while(self):
        actions.insert("while ()")
        actions.edit.left()

    def code_state_for(self):
        actions.insert("for ()")
        actions.edit.left()

    def code_state_for_each(self):
        actions.insert("foreach ()")
        actions.edit.left()

    def code_state_switch(self):
        actions.insert("switch ()")
        actions.edit.left()

    def code_state_case(self):
        actions.insert("case :")
        actions.edit.left()

    def code_state_do(self):
        actions.insert("do {")
        actions.key("enter")

    def code_state_go_to(self):
        actions.insert("goto ;")
        actions.edit.left()

    def code_state_return(self):
        actions.insert("return ;")
        actions.edit.left()

    def code_break(self):
        actions.insert("break;")

    def code_next(self):
        actions.insert("continue;")

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_protected_function(text: str):
        """Inserts protected function declaration"""
        result = "protected function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_public_function(text: str):
        """Inserts public function declaration"""
        result = "public function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_private_static_function(text: str):
        """Inserts private static function declaration"""
        result = "private static function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_protected_static_function(text: str):
        """Inserts protected static function declaration"""
        result = "protected static function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_public_static_function(text: str):
        """Inserts public static function declaration"""
        result = "public static function {}()".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()

    def code_insert_return_type(type: str):
        actions.insert(f": {type}")
