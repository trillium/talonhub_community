from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()
ctx.matches = r"""
code.language: scala
"""

# Scala Common Types
scala_common_types = {
    "boolean": "Boolean",
    "int": "Int",
    "float": "Float",
    "byte": "Byte",
    "double": "Double",
    "short": "Short",
    "long": "Long",
    "char": "Char",
    "unit": "Unit",
    "any": "Any",
    "any val": "AnyVal",
    "string": "String",
    "thread": "Thread",
    "exception": "Exception",
    "throwable": "Throwable",
    "none": "None",
    "success": "Success",
    "failure": "Failure",
}

# Scala Common Generic Types
scala_common_generic_types = {
    "array": "Array",
    "deck": "Deque",
    "future": "Future",
    "list": "List",
    "map": "Map",
    "nil": "Nil",
    "option": "Option",
    "queue": "Queue",
    "seek": "Seq",
    "set": "Set",
    "some": "Some",
    "stack": "Stack",
    "try": "Try",
}

scala_types = scala_common_types.copy()
scala_types.update(scala_common_generic_types)
ctx.lists["user.code_type"] = scala_types

# Scala Modifies
scala_modifiers = {
    "public": "public",
    "private": "private",
    "protected": "protected",
}

mod.list("scala_modifier", desc="Scala Modifiers")
ctx.lists["user.scala_modifier"] = scala_modifiers

scala_keywords = {
    "abstract": "abstract",
    "case class": "case class",
    "def": "def",
    "extends": "extends",
    "implicit": "implicit",
    "lazy val": "lazy val",
    "new": "new",
    "object": "object",
    "override": "override",
    "package": "package",
    "sealed": "sealed",
    "throw": "throw",
    "trait": "trait",
    "type": "type",
    "val": "val",
    "var": "var",
    "with": "with",
    "yield": "yield",
}

mod.list("scala_keyword", desc="Scala Keywords")
ctx.lists["user.scala_keyword"] = scala_keywords


@ctx.action_class("user")
class UserActions:
    def code_operator_lambda(self):
        actions.insert(" => ")

    def code_operator_subscript(self):
        actions.insert("()")
        actions.edit.left()

    def code_operator_assignment(self):
        actions.insert(" = ")

    def code_operator_subtraction(self):
        actions.insert(" - ")

    def code_operator_subtraction_assignment(self):
        actions.insert(" -= ")

    def code_operator_addition(self):
        actions.insert(" + ")

    def code_operator_addition_assignment(self):
        actions.insert(" += ")

    def code_operator_multiplication(self):
        actions.insert(" * ")

    def code_operator_multiplication_assignment(self):
        actions.insert(" *= ")

    def code_operator_exponent(self):
        actions.insert(" ^ ")

    def code_operator_division(self):
        actions.insert(" / ")

    def code_operator_division_assignment(self):
        actions.insert(" /= ")

    def code_operator_modulo(self):
        actions.insert(" % ")

    def code_operator_modulo_assignment(self):
        actions.insert(" %= ")

    def code_operator_equal(self):
        actions.insert(" == ")

    def code_operator_not_equal(self):
        actions.insert(" != ")

    def code_operator_greater_than(self):
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to(self):
        actions.insert(" >= ")

    def code_operator_less_than(self):
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to(self):
        actions.insert(" <= ")

    def code_operator_and(self):
        actions.insert(" && ")

    def code_operator_or(self):
        actions.insert(" || ")

    def code_operator_bitwise_and(self):
        actions.insert(" & ")

    def code_operator_bitwise_and_assignment(self):
        actions.insert(" &= ")

    def code_operator_increment(self):
        actions.insert("++")

    def code_operator_bitwise_or(self):
        actions.insert(" | ")

    def code_operator_bitwise_exclusive_or(self):
        actions.insert(" ^ ")

    def code_operator_bitwise_left_shift(self):
        actions.insert(" << ")

    def code_operator_bitwise_left_shift_assignment(self):
        actions.insert(" <<= ")

    def code_operator_bitwise_right_shift(self):
        actions.insert(" >> ")

    def code_operator_bitwise_right_shift_assignment(self):
        actions.insert(" >>= ")

    def code_self(self):
        actions.insert("this")

    def code_insert_null(self):
        actions.insert("null")

    def code_insert_is_null(self):
        actions.insert(" == null")

    def code_insert_is_not_null(self):
        actions.insert(" != null")

    def code_state_if(self):
        actions.insert("if () ")
        actions.edit.left()
        actions.edit.left()

    def code_state_else_if(self):
        actions.insert("else if () ")
        actions.edit.left()
        actions.edit.left()

    def code_state_else(self):
        actions.insert("else ")

    def code_state_switch(self):
        actions.insert("match {\n")

    def code_state_case(self):
        actions.insert("case  => ")
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()
        actions.edit.left()

    def code_state_for(self):
        actions.insert("for () ")
        actions.edit.left()
        actions.edit.left()

    def code_state_while(self):
        actions.insert("while () ")
        actions.edit.left()
        actions.edit.left()

    def code_break(self):
        actions.insert("break")

    def code_next(self):
        actions.insert("continue")

    def code_insert_true(self):
        actions.insert("true")

    def code_insert_false(self):
        actions.insert("false")

    def code_define_class(self):
        actions.insert("class ")

    def code_import(self):
        actions.insert("import ")

    def code_state_return(self):
        actions.insert("return ")

    def code_comment_line_prefix(self):
        actions.insert("// ")

    def code_comment_block(self):
        actions.insert("/*")
        actions.key("enter")
        actions.key("enter")
        actions.insert("*/")
        actions.edit.up()

    def code_comment_block_prefix(self):
        actions.insert("/*")

    def code_comment_block_suffix(self):
        actions.insert("*/")

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f": {type}")

    def code_operator_object_accessor(self):
        actions.insert(".")

    def code_default_function(text: str):
        """Inserts function declaration"""
        actions.user.code_public_function(text)

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private def {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "protected def {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "def {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)
