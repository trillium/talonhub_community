from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
code.language: csharp
"""
ctx.lists["user.code_common_function"] = {
    "integer": "int.TryParse",
    "print": "Console.WriteLine",
    "string": ".ToString",
}


@ctx.action_class("user")
class UserActions:
    def code_operator_indirection(self):
        actions.auto_insert("*")

    def code_operator_address_of(self):
        actions.auto_insert("&")

    def code_operator_structure_dereference(self):
        actions.auto_insert("->")

    def code_operator_lambda(self):
        actions.auto_insert("=>")

    def code_operator_subscript(self):
        actions.user.insert_between("[", "]")

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

    # action(user.code_operator_exponent): " ** "
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
        actions.auto_insert("this")

    def code_operator_object_accessor(self):
        actions.auto_insert(".")

    def code_insert_null(self):
        actions.auto_insert("null")

    def code_insert_is_null(self):
        actions.auto_insert(" == null ")

    def code_insert_is_not_null(self):
        actions.auto_insert(" != null")

    def code_state_if(self):
        actions.user.insert_between("if(", ")")

    def code_state_else_if(self):
        actions.user.insert_between("else if(", ")")

    def code_state_else(self):
        actions.insert("else\n{\n}\n")
        actions.key("up")

    def code_state_switch(self):
        actions.user.insert_between("switch(", ")")

    def code_state_case(self):
        actions.insert("case \nbreak;")
        actions.edit.up()

    def code_state_for(self):
        actions.auto_insert("for ")

    def code_state_for_each(self):
        actions.insert("foreach() ")
        actions.key("left")
        actions.edit.word_left()
        actions.key("space")
        actions.edit.left()

    def code_state_go_to(self):
        actions.auto_insert("go to ")

    def code_state_while(self):
        actions.user.insert_between("while(", ")")

    def code_state_return(self):
        actions.auto_insert("return ")

    def code_break(self):
        actions.auto_insert("break;")

    def code_next(self):
        actions.auto_insert("continue;")

    def code_insert_true(self):
        actions.auto_insert("true")

    def code_insert_false(self):
        actions.auto_insert("false")

    def code_define_class(self):
        actions.auto_insert("class ")

    def code_import(self):
        actions.auto_insert("using  ")

    def code_comment_line_prefix(self):
        actions.auto_insert("//")

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_static_function(text: str):
        """Inserts private static function"""
        result = "private static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "private void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_protected_static_function(text: str):
        result = "protected static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "public void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_public_static_function(text: str):
        result = "public static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)
