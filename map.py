from utils import rand
from utils import randbool
from utils import randcell
from utils import get_neighbor

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = "🟩🌲🌊🏥🏦🔥"
TREE_BONUS = 100
UPGRADE_COST = 1000
LIFE_COST = 5000
class Map:
  def __init__(self, width, height, clouds):
    self.width = width
    self.height = height
    self.cells = [[0 for i in range(width)]for j in range(height)]
    self.generate_forest(5, 10)
    self.generate_river(10)
    self.generate_river(3)
    self.generate_river(5)
    self.generate_upgrade_shop()
    self.generate_hospital()
    self.clouds = clouds

  def check_bounds(self, x, y):
    if (x < 0 or y < 0 or x >= self.height or y >= self.width):
      return False
    return True
  
  def print_map(self, helicopter):
    print("⬛" * (self.width + 2))
    for i in range(self.height):
      print("⬛", end="")
      for j in range(self.width):
        cell = self.cells[i][j]
        if self.clouds.cells[i][j] == 1:
          print("⬜", end="")
        elif self.clouds.cells[i][j] == 2:
          print("⚡", end="")
        elif (helicopter.x == i and helicopter.y == j):
          print("🚁", end="")
        elif (cell >= 0 and cell < len(CELL_TYPES)):
          print(CELL_TYPES[cell], end="")
      print("⬛")
    print("⬛" * (self.width + 2))
  
  def generate_forest(self, threshold, max_random):
    for i in range(self.height):
      for j in range(self.width):
        if randbool(threshold, max_random):
          self.cells[i][j] = 1

  def generate_tree(self):
    cell = randcell(self.width, self.height)
    cell_x, cell_y = cell[0], cell[1]

    if self.cells[cell_x][cell_y] == 0:
      self.cells[cell_x][cell_y] = 1

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

  def add_fire(self):
    cell = randcell(self.width, self.height)
    cell_x, cell_y = cell[0], cell[1]

    if self.cells[cell_x][cell_y] == 1:
      self.cells[cell_x][cell_y] = 5

  def update_fires(self):
    for i in range(self.height):
      for j in range(self.width):
        cell = self.cells[i][j]

        if cell == 5:
          self.cells[i][j] = 0

    for _ in range(10):
      self.add_fire()

  def process_helicopter(self, helicopter):
    cell = self.cells[helicopter.x][helicopter.y]
    clouds_cell = self.clouds.cells[helicopter.x][helicopter.y]
    if cell == 2:
      helicopter.tank = helicopter.max_tank
    if cell == 5 and helicopter.tank > 0:
      helicopter.tank -= 1
      helicopter.score += TREE_BONUS
      self.cells[helicopter.x][helicopter.y] = 1
    if cell == 4 and helicopter.score >= UPGRADE_COST:
      helicopter.max_tank += 1
      helicopter.score -= UPGRADE_COST
    if cell == 3 and helicopter.score >= LIFE_COST:
      helicopter.lives += 10
      helicopter.score -= LIFE_COST
    if clouds_cell == 2:
      helicopter.lives -= 1
    

  def generate_upgrade_shop(self):
    cell = randcell(self.width, self.height)
    cell_x, cell_y = cell[0], cell[1]

    if self.cells[cell_x][cell_y] != 2 and self.cells[cell_x][cell_y] != 3:
      self.cells[cell_x][cell_y] = 4
    else:
      self.generate_upgrade_shop()

  def generate_hospital(self):
    
    cell = randcell(self.width, self.height)
    cell_x, cell_y = cell[0], cell[1]
    if self.cells[cell_x][cell_y] != 2 and self.cells[cell_x][cell_y] != 4:
      self.cells[cell_x][cell_y] = 3
    else:
      self.generate_hospital()
    
