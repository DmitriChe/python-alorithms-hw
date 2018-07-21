# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'{arr} - исходный массив')
min_num = max_num = arr[0]
min_idx = max_idx = 0

for i in range(len(arr)):
    if arr[i] < min_num:
        min_num = arr[i]
        min_idx = i
    if arr[i] > max_num:
        max_num = arr[i]
        max_idx = i

spam = arr[min_idx]
arr[min_idx] = arr[max_idx]
arr[max_idx] = spam

print(f'{arr} - перестановка (варинт 1)')


# Вариант 2
arr[arr.index(max(arr))], arr[arr.index(min(arr))] = arr[arr.index(min(arr))], arr[arr.index(max(arr))]
print(f'{arr} - перестановка (варинт 2)')

