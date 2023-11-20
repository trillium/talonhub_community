app: chrome
-
tag(): browser
tag(): user.tabs

profile switch: user.chrome_mod("shift-m")

tab search: user.chrome_mod("shift-a")

tab search <user.text>$:
    browser.focus_address()
    sleep(200ms)
    user.chrome_mod("shift-a")
    
    sleep(200ms)
    insert("{text}")
    key(down)

toggle dark:
    key(alt-shift-d)