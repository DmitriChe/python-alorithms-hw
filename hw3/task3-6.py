# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

arr = [random.randint(-100, 100) for _ in range(10)]

min_num = max_num = arr[0]
min_pos = max_pos = 0
summa = 0

for i in range(len(arr)):
    if arr[i] < min_num:
        min_num = arr[i]
        min_pos = i
    if arr[i] > max_num:
        max_num = arr[i]
        max_pos = i

# вывод
print(arr)

if min_pos == max_pos:
    print('Случилось чудо! В массиве минимальный и максимальный элементы имеют одинаковые позиции!')
elif abs(min_pos - max_pos) == 1:
    print('Минимальный и максимальный элементы массива соседствуют - между ними никого нет!')
else:
    if min_pos < max_pos:
        for i in range(min_pos + 1, max_pos):
            summa += arr[i]
    else:
        for i in range(max_pos + 1, min_pos):
            summa += arr[i]

print(f'Сумма чисел между минимальным({min_num}) и максимальным({max_num}) элементами массива составляет: {summa}')
