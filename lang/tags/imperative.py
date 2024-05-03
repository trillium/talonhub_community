from talon import Context, Module, actions

c_like_ctx = Context()
mod = Module()

mod.tag(
    "code_imperative",
    desc="Tag for enabling basic imperative programming commands (loops, functions, etc)",
)
mod.tag("code_block_c_like", desc="Language uses C style code blocks, i.e. braces")

c_like_ctx.matches = """
tag: self.code_block_c_like
"""


@mod.action_class
class Actions:
    def code_block(self):
        """Inserts equivalent of {\n} for the active language, and places the cursor appropriately"""

    def code_state_if(self):
        """Inserts if statement"""

    def code_state_else_if(self):
        """Inserts else if statement"""

    def code_state_else(self):
        """Inserts else statement"""

    def code_state_do(self):
        """Inserts do statement"""

    def code_state_switch(self):
        """Inserts switch statement"""

    def code_state_case(self):
        """Inserts case statement"""

    def code_state_for(self):
        """Inserts for statement"""

    def code_state_for_each(self):
        """Inserts for each equivalent statement"""

    def code_state_go_to(self):
        """inserts go-to statement"""

    def code_state_while(self):
        """Inserts while statement"""

    def code_state_infinite_loop(self):
        """Inserts infinite loop statement"""

    def code_state_return(self):
        """Inserts return statement"""

    def code_break(self):
        """Inserts break statement"""

    def code_next(self):
        """Inserts next/continue statement"""

    def code_try_catch(self):
        """Inserts try/catch. If selection is true, does so around the selection"""


@c_like_ctx.action_class("self")
class CActions:
    def code_block(self):
        actions.user.insert_between("{", "}")
        actions.key("enter")
