from random import randint as rand

def randbool(threshold, max_random):
  return rand(0, max_random) <= threshold

def randcell(width, height):
  rand_x = rand(0, height - 1)
  rand_y = rand(0, width - 1)
  return (rand_x, rand_y) 

# 0 - ввеерх, 1- направо? 2 - вниз, 3 - налево
def get_neighbor(x, y):
  return [
    (x - 1, y),
    (x, y + 1),
    (x + 1, y),
    (x, y - 1)
  ]