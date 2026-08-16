from utils import randcell

class Helicopter:
  def __init__(self, field_width, field_height):
    self.field_width = field_width
    self.field_height = field_height
    self.x, self.y = randcell(field_width, field_height)
    self.tank = 0
    self.max_tank = 1

  def move(self, dx, dy):
    new_x, new_y = self.x + dx, self.y + dy 

    if (0 <= new_x < self.field_height and 0 <= new_y < self.field_width):
      self.x, self.y = new_x, new_y

  def print_stats(self):
    print("💧 ", self.tank, "/", self.max_tank, sep="")