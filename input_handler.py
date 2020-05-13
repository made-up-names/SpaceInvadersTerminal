import os
from pynput import keyboard
from missiles import *

ship = None
def key_on_press(key):
		global ship

		try:
			k = key.char
		except:
			k = key.name
		if (k == 'a'):
				ship.moveleft()
		elif (k == 'd'):
				ship.moveright()
		elif (k == 'space'):
				mis1(ship.r, ship.c)
		elif (k == 's'):
				mis2(ship.r, ship.c)
		elif (k == 'q'):
				os._exit(0)

def read_asynchronous_input(ship1):
	global ship
	ship = ship1
	with keyboard.Listener(on_press=key_on_press) as lis:
		lis.join()

