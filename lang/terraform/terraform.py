from talon import Context, Module, actions

ctx = Context()
mod = Module()
ctx.matches = r"""
code.language: terraform
"""

types = {
    "string": "string",
    "number": "number",
    "bool": "bool",
    "list": "list",
    "map": "map",
    "null": "null",
}

ctx.lists["user.code_type"] = types

common_properties = {
    "name": "name",
    "type": "type",
    "description": "description",
    "default": "default",
    "for each": "for_each",
    "count": "count",
    "prevent destroy": "prevent_destroy",
    "nullable": "nullable",
    "sensitive": "sensitive",
    "depends on": "depends_on",
    "provider": "provider",
    "source": "source",
}

mod.list("terraform_common_property", desc="Terraform Modifier")
ctx.lists["self.terraform_common_property"] = common_properties

module_blocks = {
    "variable": "variable",
    "output": "output",
    "provider": "provider",
    "module": "module",
}

mod.list("terraform_module_block", desc="Simple Terraform Block")
ctx.lists["self.terraform_module_block"] = module_blocks


@mod.action_class
class Actions:
    def code_terraform_module_block(text: str):
        """Inserts a new module-related block of a given type (e.g. variable, output, provider...)"""

    def code_terraform_resource(text: str):
        """Inserts a new resource block with given name"""

    def code_terraform_data_source(text: str):
        """Inserts a new data block with given name"""


@ctx.action_class("user")
class UserActions:
    def code_terraform_module_block(text: str):
        actions.user.insert_between(text + ' "', '"')

    def code_terraform_resource(text: str):
        result = f"resource \"{actions.user.formatted_text(text, 'SNAKE_CASE')}\" \"\""

        actions.insert(result)
        actions.key("left")

    def code_terraform_data_source(text: str):
        result = f"data \"{actions.user.formatted_text(text, 'SNAKE_CASE')}\" \"\""

        actions.insert(result)
        actions.key("left")

    def code_operator_assignment(self):
        actions.insert(" = ")

    def code_operator_subtraction(self):
        actions.insert(" - ")

    def code_operator_addition(self):
        actions.insert(" + ")

    def code_operator_multiplication(self):
        actions.insert(" * ")

    def code_operator_division(self):
        actions.insert(" / ")

    def code_operator_modulo(self):
        actions.insert(" % ")

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

    def code_insert_true(self):
        actions.insert("true")

    def code_insert_false(self):
        actions.insert("false")

    def code_operator_lambda(self):
        actions.insert(" => ")

    def code_insert_null(self):
        actions.insert("null")

    def code_insert_is_null(self):
        actions.insert(" == null")

    def code_insert_is_not_null(self):
        actions.insert(" != null")

    def code_comment_line_prefix(self):
        actions.insert("# ")

    def code_state_for(self):
        actions.user.insert_between("for ", " in")
