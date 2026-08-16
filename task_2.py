# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

import os
import subprocess

class Field:
  def __init__(self, width=10, height=10):
    self.width = width
    self.height = height

  def draw(self, turtle):
    for y in range(self.height):
      for x in range(self.width):
        if x == turtle.x and y == turtle.y:
          print("T", end="")
        else:
          print("*", end="")
      print()

class Turtle:
  def __init__(self, x=0, y=0, s=1):
    self.x = x
    self.y = y
    self.s = s

  def go_up(self):
    self.y -= self.s

  def go_down(self):
    self.y += self.s

  def go_left(self):
    self.x -= self.s

  def go_right(self):
    self.x += self.s

  def evolve(self):
    self.s += 1

  def degrade(self):
    if self.s > 1:
      self.s -=1

  def count_moves(self, x2, y2):
    distance_x = abs(x2 - self.x)
    distance_y = abs(y2 - self.y)

    return max((distance_x + self.s - 1) // self.s, (distance_y + self.s - 1) // self.s)

class Game:
  def __init__(self, field: "Field", turtle: "Turtle"):
    self.field = field
    self.turtle = turtle

  def show_menu(self):
    print(
      "\033[33mУправление:\033[0m\n"
      "\033[36mW\033[0m - вверх\n"
      "\033[36mS\033[0m - вниз\n"
      "\033[36mA\033[0m - влево\n"
      "\033[36mD\033[0m - вправо\n"
      "\033[36mE\033[0m - увеличить скорость\n"
      "\033[36mR\033[0m - уменьшить скорость\n"
      "\033[36mQ\033[0m - выход\n"
    )

  def console_clear(self):
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

  def render(self):
    self.field.draw(self.turtle)

  def can_move(self, x, y):
    return 0 <= x < self.field.width and 0 <= y < self.field.height

  def execute(self, command):
    if command == "w":      
      if self.can_move(self.turtle.x, self.turtle.y - self.turtle.s):
        self.turtle.go_up()
    elif command == "s":
      if self.can_move(self.turtle.x, self.turtle.y + self.turtle.s):
        self.turtle.go_down()
    elif command == "a":
      if self.can_move(self.turtle.x - self.turtle.s, self.turtle.y):
        self.turtle.go_left()
    elif command == "d":
      if self.can_move(self.turtle.x + self.turtle.s, self.turtle.y):
        self.turtle.go_right()
    elif command == "r":
      self.turtle.evolve()
    elif command == "e":
      self.turtle.degrade()


# Попробовал сделать консольную игру, а не просто задание
field = Field()
turtle = Turtle()
game = Game(field, turtle)

while True:
  game.console_clear()
  game.show_menu()
  game.render()

  command = input("\033[33mХод: \033[0m").lower()

  if command == "q":
    break

  game.execute(command)


