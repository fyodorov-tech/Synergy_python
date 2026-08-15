# Задание №3
# Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.
numbers = list(map(int, input("Введите числа через пробел: ").split()))
unique_numbers = set()

for number in numbers:
  if number in unique_numbers:
    print(f"{number}: YES")
  else:
    print(f"{number}: NO")
    unique_numbers.add(number)