# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import uniform


def merge_sort(array):

    n = len(array)
    if n < 2:  # базовый случай
        return array

    left = merge_sort(array[:n//2])  # левая половина массива (рекурсивная сортировка)
    right = merge_sort(array[n//2:n])  # правая половина массива (рекурсивная сортировка)

    i = j = 0
    res = []
    while i < len(left) or j < (len(right)):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res


arr = [round(uniform(0, 50), 2) for i in range(20)]

print(f'Исходный массив:\n{arr}\n')
print(f'Конечный массив:\n{merge_sort(arr)}\n')
