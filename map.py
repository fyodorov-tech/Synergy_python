from utils import randbool

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

  # def generate_river():
  def generate_forest(self, threshold, max_random):
    for i in range(self.height):
      for j in range(self.width):
        if randbool(threshold, max_random):
          self.cells[i][j] = 1

  # def generate_forest():

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