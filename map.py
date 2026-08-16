from utils import rand
from utils import randbool
from utils import randcell
from utils import get_neighbor

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп

CELL_TYPES = "🟩🌲🌊🏥🏦"

class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = [[0 for i in range(width)]for j in range(height)]

  def generate_river(self, max_length):
    while True:
      rand_x, rand_y = randcell(self.width, self.height)

      if self.cells[rand_x][rand_y] != 2:
        break
    
    self.cells[rand_x][rand_y] = 2
    max_length -= 1

    while max_length > 0:
      free_neighbors = []

      for x, y in get_neighbor(rand_x, rand_y):
        if self.check_bounds(x, y) and self.cells[x][y] != 2:
          free_neighbors.append((x, y))

      if not free_neighbors:
        break

      rand_x, rand_y = free_neighbors[rand(0, len(free_neighbors) - 1)]
      self.cells[rand_x][rand_y] = 2
      max_length -= 1      

  def generate_forest(self, threshold, max_random):
    for i in range(self.height):
      for j in range(self.width):
        if randbool(threshold, max_random):
          self.cells[i][j] = 1

  def print_map(self):
    print("⬛" * (self.width + 2))
    for row in self.cells:
      print("⬛", end="")
      for cell in row:
        if (cell >= 0 and cell < len(CELL_TYPES)):
          print(CELL_TYPES[cell], end="")
      print("⬛")
    print("⬛" * (self.width + 2))

  def check_bounds(self, x, y):
    if (x < 0 or y < 0 or x >= self.height or y >= self.width):
      return False
    return True

tmp = Map(20, 10)
tmp.generate_river(10)
tmp.generate_river(5)
tmp.generate_river(8)
tmp.print_map()