# Задание №2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:

# class Transport:

#   def __init__(self, name, max_speed, mileage):
#     self.name = name
#     self.max_speed = max_speed
#     self.mileage = mileage

#   def seating_capacity(self, capacity):
#     return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:

  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

  def seating_capacity(self, capacity):
    return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

  # Переопределил __str__ т. к. считаю что так удобнее выводить информацию об объекте
  def __str__(self):
    return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

class Autobus(Transport):
  def seating_capacity(self, capacity=50):
    return super().seating_capacity(capacity)

bus = Autobus("Renaul Logan", 180, 12)
print(bus)
print(bus.seating_capacity())