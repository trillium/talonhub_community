# from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui

# @ctx.action("user.noise_trigger_pop")
# def on_pop():
#     core.repeat_phrase(1)

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui, 

ctx = Context()

@ctx.action("user.noise_trigger_pop")
def on_pop():
    print("~~~~REPEATER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    core.repeat_phrase(1)

# from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui

# ctx = Context()

# @ctx.action("user.noise_trigger_pop")
# def on_pop():
#     print("~~~~REPEATER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

