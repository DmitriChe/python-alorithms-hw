# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанного в рамках домашнего задания первых трех уроков.
# (Задача: в одномерном массиве целых чисел определить два наименьших элемента.)
import functools
import cProfile
import random


# АЛГОРИТМ-1.
def find_mins_1(n):
    arr = [random.randint(-100, 100) for _ in range(n)]

    minimorum = arr[0]
    minimum = arr[1]

    for i in range(len(arr) - 1):
        if arr[i + 1] < minimorum:
            minimum = minimorum
            minimorum = arr[i + 1]
        else:
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]

    return arr, minimorum, minimum


# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_1" "task4_1.find_mins_1(10)"
# 10000 loops, best of 5:  25.7 usec per loop        n=10
# 10000 loops, best of 5:  97.4 usec per loop        n=40
# 10000 loops, best of 5: 169.0 usec per loop        n=70
# 10000 loops, best of 5: 239.0 usec per loop        n=100
# за равный прирост данных (+30) равное увеличение времени (+70) - линейная сложность алгоритма O(x)

# проверка №2 с пом. cProfile:
# cProfile.run('find_mins_1(10000)')
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.003    0.003 task4_1.py:8(find_mins_1)      n=1000
#       1    0.001    0.001    0.006    0.006 task4_1.py:8(find_mins_1)      n=2000
#       1    0.001    0.001    0.009    0.009 task4_1.py:8(find_mins_1)      n=3000
#       1    0.003    0.003    0.031    0.031 task4_1.py:8(find_mins_1)      n=10000
# линейный характер сложности алгоритма


# АЛГОРИТМ-2.
def find_mins_2(n):
    arr = sorted([random.randint(-100, 100) for _ in range(n)])

    return arr, arr[0], arr[1]

# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_1" "task4_1.find_mins_2(10)"
# 10000 loops, best of 5:  23.4 usec per loop        n=10
# 10000 loops, best of 5:  89.2 usec per loop        n=40
# 10000 loops, best of 5: 155.0 usec per loop        n=70
# 10000 loops, best of 5: 222.0 usec per loop        n=100
# за равный прирост данных (+30) равное увеличение времени (+60) - линейная сложность алгоритма O(x)
# этот алгоритм дает небольшой выйгрыш по времени, несмотря на сортировку
# следовательно алгоритм сортировки здесь работает быстрее, чем мой алгоритм поиска мин и макс

# проверка №2 с пом. cProfile:
# cProfile.run('find_mins_2(10000)')
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.003    0.003 task4_1.py:45(find_mins_2)      n=1000
#       1    0.000    0.000    0.006    0.006 task4_1.py:45(find_mins_2)      n=2000
#       1    0.000    0.000    0.009    0.009 task4_1.py:45(find_mins_2)      n=3000
#       1    0.000    0.000    0.029    0.029 task4_1.py:45(find_mins_2)      n=10000
# аналогично видим небольшой выйгрыш по времени и линейный характер сложности алгоритма
# ВЫВОД: второй алгоритм более эффективен по времени выполнения.


# АЛГОРИТМ-1 с декоратором.
@functools.lru_cache()
def find_mins_3(n):
    arr = [random.randint(-100, 100) for _ in range(n)]

    minimorum = arr[0]
    minimum = arr[1]

    for i in range(len(arr) - 1):
        if arr[i + 1] < minimorum:
            minimum = minimorum
            minimorum = arr[i + 1]
        else:
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]

    return arr, minimorum, minimum


# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_1" "task4_1.find_mins_3(10)"
# 10000 loops, best of 5: 188 nsec per loop        n=10
# 10000 loops, best of 5: 194 nsec per loop        n=40
# 10000 loops, best of 5: 185 nsec per loop        n=70
# 10000 loops, best of 5: 186 nsec per loop        n=100
# 10000 loops, best of 5: 188 nsec per loop        n=1000
# 10000 loops, best of 5: 185 nsec per loop        n=10000
# линейная сложность алгоритма O(x), причем график почти горизонтальный - время практически не зависит от объема данных
# этот алгоритм дает наибольшой выйгрыш по времени - почти в 1000 раз, при большей загрузке памяти

# проверка №2 с пом. cProfile:
cProfile.run('find_mins_3(10000)')
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.003    0.003 task4_1.py:74(find_mins_3)      n=1000
#       1    0.001    0.001    0.006    0.006 task4_1.py:74(find_mins_3)      n=2000
#       1    0.001    0.001    0.009    0.009 task4_1.py:74(find_mins_3)      n=3000
#       1    0.003    0.003    0.031    0.031 task4_1.py:74(find_mins_3)      n=10000
# линейный характер сложности алгоритма, но действие декоратора незаметно...


# АЛГОРИТМ-2 с декоратором.
@functools.lru_cache()
def find_mins_4(n):
    arr = sorted([random.randint(-100, 100) for _ in range(n)])

    return arr, arr[0], arr[1]
# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_1" "task4_1.find_mins_4(10)"
# 10000 loops, best of 5: 186 nsec per loop        n=10
# 10000 loops, best of 5: 188 nsec per loop        n=40
# 10000 loops, best of 5: 187 nsec per loop        n=70
# 10000 loops, best of 5: 184 nsec per loop        n=100
# 10000 loops, best of 5: 192 nsec per loop        n=1000
# 10000 loops, best of 5: 194 nsec per loop        n=10000
# все аналогично предыдущему варианту с декоратором

# проверка №2 с пом. cProfile:
# cProfile.run('find_mins_4(10000)')
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.003    0.003 task4_1.py:73(find_mins_4)      n=1000
#       1    0.000    0.000    0.006    0.006 task4_1.py:73(find_mins_4)      n=2000
#       1    0.000    0.000    0.009    0.009 task4_1.py:73(find_mins_4)      n=3000
#       1    0.000    0.000    0.029    0.029 task4_1.py:73(find_mins_4)      n=10000
# чудесное действие декоратора здесь почему-то не проявляется...


n = 100
x = find_mins_1(n)
y = find_mins_2(n)

print(f'{sorted(x[0])}\nДва минимальных элемента массива: {x[1]} и {x[2]}')
print(f'{y[0]}\nДва минимальных элемента массива: {y[1]} и {y[2]}')


