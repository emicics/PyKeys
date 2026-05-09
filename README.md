This library simplifies key detection with just three simple, easy-to-call values:

PyKey.key
PyKey.hotkey
PyKey.F

Key displays the currently pressed letter key along with combinations. For example:

if PyKey.key == 'a, d':
	print("The 'a' and 'd' keys are pressed in that order")`

for hotkeys:

if PyKey.hotkey == ctrl, d':
	print("You pressed Ctrl+D")

and for F:

if PyKey.F == 'F5':
	print("You pressed F5")