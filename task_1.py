# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
class Till:
  def __init__(self, cash=0):
    self.cash = cash

  def top_up(self, amount):
    self.cash += amount

  def count_1000(self):  
    return self.cash // 1000

  def take_away(self, amount):
    if self.cash < amount:
      raise ValueError("В кассе недостаточно денег")
    self.cash -= amount

  def __str__(self):
    return f"В кассе {self.cash} рублей"


till = Till()
print(till)

print(f"Количество целых тысяч в кассе: {till.count_1000()}")

till.top_up(12900)
print(till)

try:
  till.take_away(7000)  
except ValueError as error:
  print(f"Ошибка! {error}")
else:
  print(till)

