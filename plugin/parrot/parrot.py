from talon import Module, Context, cron, actions
import time

mod = Module()
state = {}
cron_jobs = {}
callbacks = {}
shush_start: float = 0

ctx = Context()
ctx.matches = r"""
mode: command
mode: dictation
"""


@ctx.action_class("user")
class UserActions:
    def noise_pop():
        actions.user.hud_add_log("event", "pop")
        
    def noise_ssss():
        actions.user.hud_add_log("event", "ssss")

    def noise_cluck():
        if not last_command_is_sleep():
            actions.core.repeat_phrase()
            actions.user.hud_add_log("event", "alviolar-click")
    
    def noise_lateral_click():
        # actions.user.cancel_in_flight_phrase
        actions.user.hud_add_log("event", "lateral-click")

    def noise_shush_start():
        actions.user.hud_add_log("event", "shush")
        global shush_start
        shush_start = time.perf_counter()
        actions.user.mouse_scroll_up()

    def noise_shush_stop():
        actions.user.abort_specific_phrases(
            ["hash", "ssh"], shush_start, time.perf_counter()
        )
        actions.user.mouse_scroll_stop()

    def noise_hiss_start():
        actions.user.hud_add_log("event", "hiss")
        actions.user.mouse_scroll_down

    def noise_hiss_stop():
        actions.user.mouse_scroll_stop()


@mod.action_class
class Actions:
    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        if name not in state:
            state[name] = active
            cron_jobs[name] = cron.after("80ms", lambda: callback(name))
        elif state[name] != active:
            cron.cancel(cron_jobs[name])
            state.pop(name)

    def noise_pop():
        """Noise pop"""

    def noise_ssss():
        """Noise ssss"""
        actions.user.hud_add_log("event", "ssss")


    def noise_cluck():
        """Noise cluck"""

    def noise_lateral_click():
        """Noise lateral click"""

    def noise_shush_start():
        """Noise shush started"""

    def noise_shush_stop():
        """Noise shush stopped"""

    def noise_hiss_start():
        """Noise hiss started"""

    def noise_hiss_stop():
        """Noise hiss stopped"""


def last_command_is_sleep():
    cmd, _ = actions.core.last_command()
    return cmd.script.code.startswith("user.alon_sleep()")


def callback(name: str):
    active = state.pop(name)
    callbacks[name](active)


def on_shush(active: bool):
    if active:
        actions.user.debug("shush:start")
        actions.user.noise_shush_start()
    else:
        actions.user.debug("shush:stop")
        actions.user.noise_shush_stop()


def on_hiss(active: bool):
    if active:
        actions.user.debug("hiss:start")
        actions.user.noise_hiss_start()
    else:
        actions.user.debug("hiss:stop")
        actions.user.noise_hiss_stop()


callbacks["shush"] = on_shush
callbacks["hiss"] = on_hiss