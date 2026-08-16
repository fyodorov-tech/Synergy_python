# Задание №1

# Есть родительский класс:
# class Transport:

#   def __init__(self, name, max_speed, mileage):
      # self.name = name
      # self.max_speed = max_speed
      # self.mileage = mileage
 
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

  def __str__(self):
    return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

autobus = Transport("Renaul Logan", 180, 12)

print(autobus)