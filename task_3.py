# Задание №3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
min_invest_sum = int(input("Введите минимальную сумму инвестиций:\n"))
michael_money = int(input("Введите количество денег Майкла:\n"))
ivan_money = int(input("Введите количество денег Ивана:\n"))

if michael_money  >= min_invest_sum and ivan_money >= min_invest_sum:
  print(2)
elif michael_money >= min_invest_sum:
    print("Michael")
elif ivan_money >= min_invest_sum:
   print("Ivan")
elif michael_money + ivan_money >= min_invest_sum:
      print(1)
else:
    print(0)    