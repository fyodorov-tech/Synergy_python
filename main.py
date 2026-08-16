from map import Map
import time
import os
import subprocess

TICK_SLEEP = 0.05

def clear():
  subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

tmp = Map(20, 10)
tmp.generate_forest(5, 10)
tmp.generate_river(10)
tmp.generate_river(5)
tmp.generate_river(8)

tick = 1
while True:
  clear()
  print("TICK", tick)
  tmp.print_map()
  tick += 1
  time.sleep(TICK_SLEEP)