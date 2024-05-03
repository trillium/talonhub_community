from talon import Context, Module, actions

c_like_ctx = Context()
mod = Module()

mod.tag("code_comment_block", desc="Tag for enabling generic block comment commands")
mod.tag("code_comment_block_c_like", desc="Denotes usage of C-style block comments")

c_like_ctx.matches = """
tag: user.code_comment_block_c_like
"""
c_like_ctx.tags = ["user.code_comment_block"]


@mod.action_class
class Actions:
    def code_comment_block(self):
        """Block comment"""

    def code_comment_block_prefix(self):
        """Block comment start syntax"""

    def code_comment_block_suffix(self):
        """Block comment end syntax"""


@c_like_ctx.action_class("user")
class CActions:
    def code_comment_block(self):
        actions.insert("/*\n\n*/")
        actions.edit.up()

    def code_comment_block_prefix(self):
        actions.auto_insert("/*")

    def code_comment_block_suffix(self):
        actions.auto_insert("*/")
