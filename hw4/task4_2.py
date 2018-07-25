# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
import cProfile


def eratos(nth):
    n = 3

    while True:
        sieve = [i for i in range(n)]

        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i * 2

                while j < n:
                    sieve[j] = 0
                    j += i

        b = [i for i in sieve if i != 0]
        if len(b) == nth:
            return b[-1]
        else:
            n += 1

# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_2" "task4_2.eratos(10)"
# 10000 loops, best of 5:   2.5 usec per loop - для 1-го элемента
# 10000 loops, best of 5:   5.2 usec per loop - для 2-го элемента
# 10000 loops, best of 5:  11.8 usec per loop - для 3-го элемента
# 10000 loops, best of 5:  20.0 usec per loop - для 4-го элемента
# 10000 loops, best of 5:  40.0 usec per loop - для 5-го элемента
# 10000 loops, best of 5:  52.7 usec per loop - для 6-го элемента
# 10000 loops, best of 5:  83.8 usec per loop - для 7-го элемента
# 10000 loops, best of 5: 101.0 usec per loop - для 8-го элемента
# 10000 loops, best of 5: 140.0 usec per loop - для 9-го элемента
# 10000 loops, best of 5: 212.0 usec per loop - для 10-го элемента
# 10000 loops, best of 5: 1.12 msec per loop - для 20-го элемента
# При увеличении значения в 2 раза, время увеличивается в 5 раз, т.е. время растет более чем вдовое быстрее, данные

# проверка №2 с пом. cProfile:
# cProfile.run('eratos(900)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.057    0.057    0.068    0.068 task4_2.py:7(eratos)   -   для n=100
#    540    0.005    0.000    0.005    0.000 task4_2.py:11(<listcomp>)
#      1    0.319    0.319    0.374    0.374 task4_2.py:7(eratos)   -   для n=200
#   1222    0.025    0.000    0.025    0.000 task4_2.py:11(<listcomp>)
#      1    0.861    0.861    1.005    1.005 task4_2.py:7(eratos)   -   для n=300
#   1986    0.067    0.000    0.067    0.000 task4_2.py:11(<listcomp>)
#      1    1.686    1.686    1.960    1.960 task4_2.py:7(eratos)   -   для n=400
#   2740    0.125    0.000    0.125    0.000 task4_2.py:11(<listcomp>)
#      1    2.904    2.904    3.366    3.366 task4_2.py:7(eratos)   -   для n=500
#   3570    0.211    0.000    0.211    0.000 task4_2.py:11(<listcomp>)
#      1    4.479    4.479    5.182    5.182 task4_2.py:7(eratos)   -   для n=600
#   4408    0.321    0.000    0.321    0.000 task4_2.py:11(<listcomp>)
#      1    6.445    6.445    7.456    7.456 task4_2.py:7(eratos)   -   для n=700
#   5278    0.460    0.000    0.460    0.000 task4_2.py:11(<listcomp>)
#      1    8.936    8.936   10.289   10.289 task4_2.py:7(eratos)   -   для n=800
#   6132    0.650    0.000    0.650    0.000 task4_2.py:11(<listcomp>)
#      1   11.403   11.403   13.151   13.151 task4_2.py:7(eratos)   -   для n=900
#   6996    0.802    0.000    0.802    0.000 task4_2.py:11(<listcomp>)
#      1   14.705   14.705   17.120   17.120 task4_2.py:7(eratos)   -   для n=1000
#   7918    1.032    0.000    1.032    0.000 task4_2.py:11(<listcomp>)
#      1   73.393   73.393   84.078   84.078 task4_2.py:7(eratos) - для n=2000
# Равномерное увеличение значения вызывает почти линейное увеличение циклов генератора списков
# При увеличении знач в 2 раза, время алгоритма увеличивается в 5 раз, т.е. растет более чем вдовое быстрее данных
# ВЫВОД:


def find_nth_simple(nth):
    count = 1
    candidate = 2

    while count < nth:
        candidate += 1
        for i in range(candidate - 1, 1, -1):
            if candidate % i == 0:
                break
            if i == 2:
                count += 1

    return candidate
# проверка №1 с пом. timeit в терминале:
# >python -m timeit -n 10000 -s "import task4_2" "task4_2.find_nth_simple(10)"
# 10000 loops, best of 5:   0.31 usec per loop - для 1-го элемента
# 10000 loops, best of 5:   1.13 usec per loop - для 2-го элемента
# 10000 loops, best of 5:   3.00 usec per loop - для 3-го элемента
# 10000 loops, best of 5:   5.26 usec per loop - для 4-го элемента
# 10000 loops, best of 5:  10.80 usec per loop - для 5-го элемента
# 10000 loops, best of 5:  14.20 usec per loop - для 6-го элемента
# 10000 loops, best of 5:  21.90 usec per loop - для 7-го элемента
# 10000 loops, best of 5:  26.30 usec per loop - для 8-го элемента
# 10000 loops, best of 5:  36.10 usec per loop - для 9-го элемента
# 10000 loops, best of 5:  53.20 usec per loop - для 10-го элемента
# 10000 loops, best of 5: 264.00 usec per loop - для 20-го элемента
# При увеличении значения в 2 раза, время увеличивается в 5 раз, как и в первом алгоритме,
# однако сам алгоритм отрабатывает быстрее первого в 4 раза

# проверка №2 с пом. cProfile:
# cProfile.run('find_nth_simple(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.014    0.014    0.014    0.014 task4_2.py:74(find_nth_simple) - для n=100
#      1    0.074    0.074    0.074    0.074 task4_2.py:74(find_nth_simple) - для n=200
#      1    0.182    0.182    0.182    0.182 task4_2.py:74(find_nth_simple) - для n=300
#      1    0.349    0.349    0.349    0.349 task4_2.py:74(find_nth_simple) - для n=400
#      1    0.596    0.596    0.596    0.596 task4_2.py:74(find_nth_simple) - для n=500
#      1    0.917    0.917    0.917    0.917 task4_2.py:74(find_nth_simple) - для n=600
#      1    1.319    1.319    1.319    1.319 task4_2.py:74(find_nth_simple) - для n=700
#      1    1.788    1.788    1.788    1.788 task4_2.py:74(find_nth_simple) - для n=800
#      1    2.326    2.326    2.326    2.326 task4_2.py:74(find_nth_simple) - для n=900
#      1    2.979    2.979    2.979    2.979 task4_2.py:74(find_nth_simple) - для n=1000
#      1   14.385   14.385   14.385   14.385 task4_2.py:74(find_nth_simple) - для n=2000
# При увеличении значения в 2 раза, время увеличивается в 5 раз, как и в первом алгоритме, но
# этот алгоритм не требует на каждом шаге предварительной генерации списка чисел, для "прокалывания" -
# все вычисляется за 1 проход, поэтому функция выполняется в 6 раз быстрее

# Сложность алгоритма. Мне кажется, что оба алгоритма имеют одинаковую сложность и это либо o(N*M) либо квадратичная
# Я больше склоняюсь к первой, т.к.

# ВЫВОД: мой алгоритм эффективнее алгоритма Эратосфена. Что и не удивительно - ведь сколько воды утекло с тех пор.
# Земля полегчала и стала вращаться быстрее, ускорилось время, а с ним и все процессы.


nth = int(input('Введите номер простого числа: '))
if nth > 0:
    # print(f'Искомое простое число: {find_nth_simple(nth)}')
    print(f'Искомое простое число: {eratos(nth)} - по Эратосфену')
    print(f'Искомое простое число: {find_nth_simple(nth)} - по мне')
else:
    print('ОШИБКА! Введен некорректный номер')

