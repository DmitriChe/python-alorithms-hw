# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

arr = [random.randint(-100, 100) for _ in range(10)]

minimorum = arr[0]
minimum = arr[1]

for i in range(len(arr) - 1):
    if arr[i + 1] < minimorum:
        minimum = minimorum
        minimorum = arr[i + 1]
    else:
        if arr[i + 1] < minimum:
            minimum = arr[i + 1]

# вывод
print(f'{arr} - исходный массив')
print(f'{sorted(arr)} - отсортированный для наглядности')
print(f'Два минимальных элемента массива: {minimorum} и {minimum}')
