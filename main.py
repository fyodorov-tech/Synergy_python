from map import Map
from helicopter import Helicopter
import time
import os
import subprocess
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 20, 10
MOVES = {"w": (-1, 0), "d": (0, 1), "s": (1, 0), "a": (0, -1), "ц": (-1, 0), "в": (0, 1), "ы": (1, 0), "ф": (0, -1)}

def clear():
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
  # print("\033[H", end="")

def process_key(key):
  if not hasattr(key, "char") or key.char is None:
    return

  global helicopter

  ch = key.char.lower()

  if ch in MOVES.keys():
    dx, dy = MOVES[ch][0], MOVES[ch][1]
    helicopter.move(dx, dy)
    
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False    

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

field = Map(MAP_WIDTH, MAP_HEIGHT)

helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)

tick = 1

while True:
  clear()
  field.process_helicopter(helicopter)
  helicopter.print_stats()
  field.print_map(helicopter)
  print("TICK", tick)
  tick += 1
  time.sleep(TICK_SLEEP)

  if (tick % TREE_UPDATE == 0):
    field.generate_tree()

  if (tick % FIRE_UPDATE == 0):
    field.update_fires()