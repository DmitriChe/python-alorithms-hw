# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

arr = [random.randint(-100, 100) for _ in range(100)]

max_negative = float('-inf')
pos = -1

for i in range(len(arr)):
    if max_negative < arr[i] < 0:
        max_negative = arr[i]
        pos = i

# вывод
print(arr)
if pos == -1:
    print('Отрицательных чисел в массиве нет!')
else:
    print(f'Максимальное отрицательное число {max_negative} стоит на {pos}-й позиции')
