tag: user.mouse_grid_showing
-
<user.number_key>: user.grid_narrow(number_key)
grid (off | close | hide): user.grid_close()

grid reset: user.grid_reset()

grid back: user.grid_go_back()

^<user.letter>$: user.grid_narrow_letter(letter)
^<user.letter> <user.letter>$: user.grid_narrow_letter(letter)
^<user.letter>+$: user.grid_narrow_list(letter_list)
