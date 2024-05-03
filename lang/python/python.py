import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: python
"""
ctx.lists["user.code_common_function"] = {
    "enumerate": "enumerate",
    "integer": "int",
    "length": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
}

"""a set of fields used in python docstrings that will follow the
reStructuredText format"""
docstring_fields = {
    "class": ":class:",
    "function": ":func:",
    "parameter": ":param:",
    "raise": ":raise:",
    "returns": ":return:",
    "type": ":type:",
    "return type": ":rtype:",
    # these are sphinx-specific
    "see also": ".. seealso:: ",
    "notes": ".. notes:: ",
    "warning": ".. warning:: ",
    "todo": ".. todo:: ",
}

mod.list("python_docstring_fields", desc="python docstring fields")
ctx.lists["user.python_docstring_fields"] = docstring_fields

ctx.lists["user.code_type"] = {
    "boolean": "bool",
    "integer": "int",
    "string": "str",
    "none": "None",
    "dick": "Dict",
    "float": "float",
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

ctx.lists["user.code_keyword"] = {
    "break": "break",
    "continue": "continue",
    "class": "class ",
    "return": "return ",
    "import": "import ",
    "null": "None",
    "none": "None",
    "true": "True",
    "false": "False",
    "yield": "yield ",
    "from": "from ",
}

exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
mod.list("python_exception", desc="python exceptions")
ctx.lists["user.python_exception"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)).lower(): exception
    for exception in exception_list
}


@ctx.action_class("user")
class UserActions:
    def code_operator_lambda(self):
        actions.user.insert_between("lambda ", ": ")

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
        actions.auto_insert(" and ")

    def code_operator_or(self):
        actions.auto_insert(" or ")

    def code_operator_in(self):
        actions.auto_insert(" in ")

    def code_operator_not_in(self):
        actions.auto_insert(" not in ")

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
        actions.auto_insert("None")

    def code_insert_is_null(self):
        actions.auto_insert(" is None")

    def code_insert_is_not_null(self):
        actions.auto_insert(" is not None")

    def code_state_if(self):
        actions.user.insert_between("if ", ":")

    def code_state_else_if(self):
        actions.user.insert_between("elif ", ":")

    def code_state_else(self):
        actions.insert("else:")
        actions.key("enter")

    def code_state_switch(self):
        actions.user.insert_between("match ", ":")

    def code_state_case(self):
        actions.user.insert_between("case ", ":")

    def code_state_for(self):
        actions.auto_insert("for ")

    def code_state_for_each(self):
        actions.user.insert_between("for ", " in ")

    def code_state_while(self):
        actions.user.insert_between("while ", ":")

    def code_define_class(self):
        actions.auto_insert("class ")

    def code_import(self):
        actions.auto_insert("import ")

    def code_comment_line_prefix(self):
        actions.auto_insert("# ")

    def code_state_return(self):
        actions.insert("return ")

    def code_insert_true(self):
        actions.auto_insert("True")

    def code_insert_false(self):
        actions.auto_insert("False")

    def code_comment_documentation(self):
        actions.user.insert_between('"""', '"""')

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "def _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "def {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")
