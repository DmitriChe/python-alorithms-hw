# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

m = 5
n = 4
row_sum = 0
matrix = [[int(input('Введите элемент матрицы: ')) for _ in range(n - 1)] for _ in range(m)]

for i in range(m):
    for j in range(n - 1):
        row_sum += matrix[i][j]
    matrix[i].append(row_sum)
    row_sum = 0

# вывод
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()
