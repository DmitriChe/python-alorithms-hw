# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
# - сортировку сделать в виде функции
# - ускорить алгоритм сортировки, данный на уроке
from random import randint


def bubble_sort(array, direction=True):

    for i in range(1, len(array)):

        done = True
        for j in range(len(array) - i):

            if direction:
                if array[j] > array[j + 1]:
                    done = False  # флаг неупорядоченности
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] < array[j + 1]:
                    done = False  # флаг неупорядоченности
                    array[j], array[j + 1] = array[j + 1], array[j]
        if done:
            break  # остановка, в случае, если все элементы уже упорядочены
        # print(array)  # отладочная строка

    return array


arr = [randint(-100, 99) for i in range(20)]
print(f'Исходный массив:\n{arr}\n')
print(f'По возрастанию:\n{bubble_sort(arr)}\n')
print(f'По убыванию:\n{bubble_sort(arr, False)}\n')
