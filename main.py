import input_handler 
from spaceship import *
from board import *
from missiles import *
from aliens import *
from pynput import keyboard

# Main code
ship = spaceship(8, 1)
board = board1()
board.counter()
aliens.spawn()
input_handler.read_asynchronous_input(ship)

