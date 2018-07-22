# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

m = 5
n = 4
matrix = [[random.randint(-100, 100) for _ in range(n)] for _ in range(m)]

max_elem = float('-inf')

for i in range(n):
    col_min = matrix[0][i]

    for j in range(m):
        if matrix[j][i] < col_min:
            col_min = matrix[j][i]

    if col_min > max_elem:
        max_elem = col_min

# вывод
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

print(f'Максимальный из минимальных элементов столбцов матрицы: {max_elem}')
