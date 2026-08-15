# Задание №2
# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False
word = input("Введите слово, состоящее из маленьких латинскик букв:\n")

a  = word.count("a") 
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

volwes_count = a + e + i + o + u
consonant_count = len(word) - volwes_count

print(f"Наличие следующих гласных в слове '{word}':")
print(f"a - {a if a > 0 else False}")
print(f"e - {e if e > 0 else False}")
print(f"i - {i if i > 0 else False}")
print(f"o - {o if o > 0 else False}")
print(f"u - {u if u > 0 else False}")