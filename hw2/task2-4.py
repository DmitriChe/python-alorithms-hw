# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

item = 1
summa = 0

n = int(input('Введите число элементов последовательности для их суммирования: '))

for i in range(n):
    summa += item
    item /= -2

print(f'Сумма {n} элементов последовательности равна: {summa}')
