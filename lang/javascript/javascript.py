from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: javascript
code.language: typescript
code.language: javascriptreact
code.language: typescriptreact
"""

ctx.lists["user.code_common_function"] = {
    "abs": "Math.abs",
    "entries": "Object.entries",
    "fetch": "fetch",
    "floor": "Math.floor",
    "from entries": "Object.fromEntries",
    "keys": "Object.keys",
    "log": "console.log",
    "max": "Math.max",
    "min": "Math.min",
    "print": "console.log",
    "round": "Math.round",
    "values": "Object.values",
}

mod.list("code_common_member_function", "Function to use in a dotted chain, eg .foo()")

ctx.lists["user.code_common_member_function"] = {
    "catch": "catch",
    "concat": "concat",
    "filter": "filter",
    "finally": "finally",
    "find": "find",
    "flat map": "flatMap",
    "for each": "forEach",
    "join": "join",
    "includes": "includes",
    "map": "map",
    "pop": "pop",
    "push": "push",
    "reduce": "reduce",
    "slice": "slice",
    "some": "some",
    "split": "split",
    "substring": "substring",
    "then": "then",
}

ctx.lists["user.code_keyword"] = {
    "a sink": "async ",
    "await": "await ",
    "break": "break",
    "class": "class ",
    "const": "const ",
    "continue": "continue",
    "default": "default ",
    "export": "export ",
    "false": "false",
    "function": "function ",
    "import": "import ",
    "let": "let ",
    "new": "new ",
    "null": "null",
    "private": "private ",
    "protected": "protected ",
    "public": "public ",
    "return": "return ",
    "throw": "throw ",
    "true": "true",
    "try": "try ",
    "undefined": "undefined",
    "yield": "yield ",
}


@ctx.action_class("user")
class UserActions:
    def code_insert_is_not_null(self):
        actions.auto_insert(" !== null")

    def code_insert_is_null(self):
        actions.auto_insert(" === null")

    def code_state_if(self):
        actions.user.insert_between("if (", ")")

    def code_state_else_if(self):
        actions.user.insert_between(" else if (", ")")

    def code_state_else(self):
        actions.user.insert_between(" else {", "}")
        actions.key("enter")

    def code_self(self):
        actions.auto_insert("this")

    def code_operator_object_accessor(self):
        actions.auto_insert(".")

    def code_state_while(self):
        actions.user.insert_between("while (", ")")

    def code_state_do(self):
        actions.auto_insert("do ")

    def code_state_return(self):
        actions.insert("return ")

    def code_state_for(self):
        actions.user.insert_between("for (", ")")

    def code_state_switch(self):
        actions.user.insert_between("switch (", ")")

    def code_state_case(self):
        actions.user.insert_between("case ", ":")

    def code_state_go_to(self):
        actions.auto_insert("")

    def code_import(self):
        actions.auto_insert("import ")

    def code_define_class(self):
        actions.auto_insert("class ")

    def code_state_for_each(self):
        actions.user.insert_between(".forEach(", ")")

    def code_break(self):
        actions.auto_insert("break;")

    def code_next(self):
        actions.auto_insert("continue;")

    def code_insert_true(self):
        actions.auto_insert("true")

    def code_insert_false(self):
        actions.auto_insert("false")

    def code_insert_null(self):
        actions.auto_insert("null")

    def code_operator_lambda(self):
        actions.auto_insert(" => ")

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

    def code_or_operator_assignment(self):
        actions.auto_insert(" ||= ")

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

    def code_comment_line_prefix(self):
        actions.auto_insert("//")

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        """Inserts function declaration without modifiers"""
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_private_static_function(text: str):
    #     """Inserts private static function"""
    #     result = "private static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_protected_static_function(text: str):
    #     result = "protected static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_protected_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_public_static_function(text: str):
    #     result = "public static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_public_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)
