import random 

def generate_matrix(rows, columns, min_value=1, max_value=10):
  matrix = []

  for _ in range(rows):
    row = []

    for _ in range(columns):
      row.append(random.randint(min_value, max_value))

    matrix.append(row)

  return matrix

def sum_matrix(matrix_1, matrix_2):

  if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
    raise ValueError("Матрицы должны быть одной размерности!")
  
  result = []

  for i in range(len(matrix_1)):
    row = []

    for j in range(len(matrix_1[i])):
      row.append(matrix_1[i][j] + matrix_2[i][j])

    result.append(row)

  return result

def print_matrix(matrix, column_width = 3):
  for row in matrix:
    for el in row:
      print(str(el).ljust(column_width), end=" ")

    print()

# Беру размерность 3, чтобы вывод не был огромным. Взять можно любую размерность
first_matrix = generate_matrix(3, 3)
second_matrix = generate_matrix(3, 3)

print(f"\033[33mFirst matrix:\033[0m")
print_matrix(first_matrix)
print()

print(f"\033[33mSecond matrix:\033[0m")
print_matrix(second_matrix)
print()


try:
  result_matrix = sum_matrix(first_matrix, second_matrix)

  print(f"\033[33mSum first matrix and second matrix:\033[0m")
  print_matrix(result_matrix)

except ValueError as error:
  print(f"\033[31mОшибка! {error}\033[0m")








