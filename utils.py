from random import randint as rand

def randbool(threshold, max_random):
  return rand(0, max_random) <= threshold

def randcell(width, height):
  rand_width = rand(0, width)
  rand_height = rand(0, height)

  return (rand_height, rand_width) 