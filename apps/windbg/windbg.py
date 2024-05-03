from talon import Context, Module, actions

mod = Module()
mod.tag("windbg", "tag to enabled windbg related functionality")

# global context for enabling and disabling user.gdb tag
ctx_global = Context()

# user.windbg-specific context
ctx_windbg_enabled = Context()
ctx_windbg_enabled.matches = r"""
tag: user.windbg
"""

ctx_windbg_enabled.lists["self.windows_dlls"] = {
    "core": "ntdll",
    "en tea": "ntdll",
    "user": "user32",
}


@mod.capture(rule="{self.windows_dlls}")
def windows_dlls(m) -> str:
    "Return an register"
    return m.windows_dlls


@mod.action_class
class Actions:
    def windbg_enable(self):
        """Enables the windbg tag"""
        ctx_global.tags = ["user.windbg"]

    def windbg_disable(self):
        """Disables the windbg tag"""
        ctx_global.tags = []


# XXX - trigger alt-1 to hit command window for necessary commands?
# ex: user.windbg_insert_in_cmd()
#    edit.left()
@ctx_windbg_enabled.action_class("user")
class UserActions:
    ##
    # Generic debugger actions
    ##

    # Code execution
    def debugger_step_into(self):
        actions.key("f8")

    def debugger_step_over(self):
        actions.key("f10")
        # XXX -

    def debugger_step_line(self):
        actions.auto_insert("")

    def debugger_step_over_line(self):
        actions.auto_insert("")

    def debugger_step_out(self):
        actions.key("shift-f11")

    def debugger_continue(self):
        actions.key("f5")

    def debugger_stop(self):
        actions.key("shift-f5")

    def debugger_restart(self):
        actions.key("ctrl-shift-f5")

    def debugger_detach(self):
        actions.insert(".detach")
        # Registers

    def debugger_show_registers(self):
        actions.key("r enter")

    def debugger_get_register(self):
        actions.insert("r @")

    def debugger_set_register(self):
        actions.user.insert_between("set $@", "=")
        # Breakpoints

    def debugger_show_breakpoints(self):
        actions.insert("bl\n")

    def debugger_add_sw_breakpoint(self):
        actions.insert("bp ")

    def debugger_add_hw_breakpoint(self):
        actions.insert("ba e 1 ")

    def debugger_break_now(self):
        actions.key("ctrl-break")

    def debugger_clear_all_breakpoints(self):
        actions.insert("bc *\n")

    def debugger_clear_breakpoint(self):
        actions.insert("bc ")

    def debugger_enable_all_breakpoints(self):
        actions.insert("be *\n")

    def debugger_enable_breakpoint(self):
        actions.insert("be ")

    def debugger_disable_all_breakpoints(self):
        actions.insert("bd *\n")

    def debugger_disable_breakpoint(self):
        actions.insert("bd ")
        # Navigation

    def debugger_goto_address(self):
        actions.insert("ctrl-g")

    def debugger_goto_clipboard(self):
        actions.insert("ctrl-g")
        actions.edit.paste()
        actions.key("enter")

    def debugger_goto_highlighted(self):
        actions.insert("ctrl-g")
        actions.edit.copy()
        actions.edit.paste()
        actions.key("enter")
        # Memory inspection

    def debugger_backtrace(self):
        actions.key("k enter")

    def debugger_disassemble(self):
        actions.key("u space")

    def debugger_disassemble_here(self):
        actions.key("u enter")

    def debugger_disassemble_clipboard(self):
        actions.key("u space")
        actions.edit.paste()
        actions.key("enter")

    def debugger_dump_ascii_string(self):
        actions.insert("da ")

    def debugger_dump_unicode_string(self):
        actions.insert("du ")

    def debugger_dump_pointers(self):
        actions.insert("dps ")

    def debugger_list_modules(self):
        actions.insert("lm\n")
        # Registers XXX

    def debugger_inspect_type(self):
        actions.insert("dt ")
        # Convenience

    def debugger_clear_line(self):
        actions.key("ctrl-a backspace")
        ##
        # Windbg specific functionality
        ##

    def debugger_clear_breakpoint_id(number_small: int):
        actions.insert(f"bc {number_small}\n")

    def debugger_disable_breakpoint_id(number_small: int):
        actions.insert(f"bd {number_small}\n")

    def debugger_enable_breakpoint_id(number_small: int):
        actions.insert(f"be {number_small}\n")
