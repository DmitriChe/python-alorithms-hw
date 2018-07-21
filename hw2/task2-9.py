# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_sum = 0

n_nums = int(input('Введите количество чисел последовательности: '))

for i in range(n_nums):
    this_number = number = int(input(f'Введите {i + 1}-е натуральное число: '))
    summa = 0;

    while number > 0:
        summa += number % 10
        number //= 10

    if summa > max_sum:
        max_sum = summa
        super_num = this_number

print(f'Число {super_num} обладает максимальной суммой цифр: {max_sum}')
