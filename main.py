from map import Map
import time
import os
import subprocess

TICK_SLEEP = 0.05
TREE_UPDATE = 50

def clear():
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

tmp = Map(20, 10)
tmp.generate_forest(5, 10)
tmp.generate_river(10)
tmp.generate_river(5)
tmp.generate_river(8)
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()
tmp.add_fire()

tick = 1

while True:
  clear()
  print("TICK", tick)
  tmp.print_map()
  tick += 1
  time.sleep(TICK_SLEEP)

  if (tick % TREE_UPDATE == 0):
    tmp.generate_tree()