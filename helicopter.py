from utils import randcell

class Helicopter:
  def __init__(self, field_width, field_height):
    self.field_width = field_width
    self.field_height = field_height
    self.x, self.y = randcell(field_width, field_height)
    self.tank = 0
    self.max_tank = 1
    self.score = 0
    self.lives = 20

  def move(self, dx, dy):
    new_x, new_y = self.x + dx, self.y + dy 

    if (0 <= new_x < self.field_height and 0 <= new_y < self.field_width):
      self.x, self.y = new_x, new_y

  def print_stats(self):
    print("💧 ", self.tank, "/", self.max_tank, sep="", end = " | ")
    print("🏆" , self.score, end=" | ")
    print("💛" , self.lives)

  def export_data(self):
    return {
      "score": self.score,
      "lives": self.lives,
      "x": self.x,
      "y": self.y,
      "tank": self.tank,
      "max_tank": self.max_tank
    }

  def import_data(self, data):
    self.x, self.y = data["x"] or 0, data["y"] or 0
    self.tank = data["tank"] or 0
    self.max_tank = data["max_tank"] or 1
    self.lives = data["lives"] or 3
    self.score = data["score"] or 0