from map import Map
from helicopter import Helicopter
from clouds import Clouds
import time
import os
import subprocess
import json
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_WIDTH, MAP_HEIGHT = 20, 10
MOVES = {"w": (-1, 0), "d": (0, 1), "s": (1, 0), "a": (0, -1), "ц": (-1, 0), "в": (0, 1), "ы": (1, 0), "ф": (0, -1)}

def clear():
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
  # print("\033[H", end="")

def game_over():
  print(f"\033[31m########################################\033[0m")
  print()
  print(f"\033[31m     GAME OVER,\033[0m YOUR SCORE IS \033[33m{helicopter.score}")
  print()
  print(f"\033[31m########################################\033[0m")

def process_key(key):
  if not hasattr(key, "char") or key.char is None:
    return

  global helicopter, clouds, field, tick

  ch = key.char.lower()

  if ch in MOVES.keys():
    dx, dy = MOVES[ch][0], MOVES[ch][1]
    helicopter.move(dx, dy)
  elif ch == "f" or ch == "а":
    data = {
      "helicopter": helicopter.export_data(),
      "clouds": clouds.export_data(),
      "field": field.export_data(),
      "tick": tick
    }
    with open("level.json", "w") as lvl:
      json.dump(data, lvl)
  elif ch == "g" or ch == "п":
    with open("level.json", "r") as lvl:
      data = json.load(lvl) 
      helicopter.import_data(data["helicopter"])
      tick = data["tick"] or 1
      field.import_data(data["field"])
      clouds.import_data(data["clouds"])

  
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)
field = Map(MAP_WIDTH, MAP_HEIGHT, clouds)
helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)
tick = 1

while True:
  clear()

  field.process_helicopter(helicopter)

  if helicopter.lives <= 0:
    clear()
    game_over()
    break  

  helicopter.print_stats()
  field.print_map(helicopter)
  print("TICK", tick)
  tick += 1
  time.sleep(TICK_SLEEP)

  if (tick % TREE_UPDATE == 0):
    field.generate_tree()

  if (tick % FIRE_UPDATE == 0):
    field.update_fires()

  if (tick % CLOUDS_UPDATE == 0):
      clouds.update()