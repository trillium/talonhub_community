tag: user.mouse_grid_showing
-
<<<<<<< HEAD
^<user.letter>$: user.grid_narrow_letter(letter)
^<user.letter> <user.letter>$: user.grid_narrow_letter(letter)
^<user.letter>+$: user.grid_narrow_list(letter_list)
=======
# Force prefixed numbers elsewhere in the config, which allows unprefixed use below
tag(): user.prefixed_numbers
<user.number_key>: user.grid_narrow(number_key)
>>>>>>> 54ce69d2fb6ba1ed44759a14daad9ceef933323c
grid off: user.grid_close()

[grid] reset: user.grid_reset()

grid back: user.grid_go_back()
