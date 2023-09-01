#defines the commands that sleep/wake Talon
mode: all
-
^(welcome back)+$:
    user.mouse_wake()
    # user.history_enable()
    user.talon_mode()


# key(f):
#     print("f")
#     app.notify("f")

# key(capslock):
#     speech.toggle()


key(cmd-alt-shift-esc): speecah.toggle()
key(ctrl-shift-esc): speech.toggle()
key(cmd-ctrl-alt-shift-esc): speech.toggle()
# key(qq): key(f19)
key(f19): speech.toggle()

^sleep all [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^talon sleep [<phrase>]$: speech.disable()
^(talon wake)+$: speech.enable()

drowse [<phrase>]$: speech.disable()
drowse <phrase> resume$: skip()