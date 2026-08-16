from map import Map
import time
import os
import subprocess

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 20, 10

def clear():
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

field = Map(MAP_WIDTH, MAP_HEIGHT)
field.generate_forest(5, 10)
field.generate_river(10)
field.generate_river(5)
field.generate_river(8)

tick = 1

while True:
  clear()
  print("TICK", tick)
  field.print_map()
  tick += 1
  time.sleep(TICK_SLEEP)

  if (tick % TREE_UPDATE == 0):
    field.generate_tree()

  if (tick % FIRE_UPDATE == 0):
    field.update_fires()