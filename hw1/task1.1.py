# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1EKRgDPysjgvrihKp9si-Q9Fpcc2srlRf/view?usp=sharing

str_num = input('Введите трёхзначное целое число: ')

a = int(str_num[0])
b = int(str_num[1])
c = int(str_num[2])

summ = a + b + c
mult = a * b * c

print(f'Сумма цифр числа равна {summ}, проиведение равно {mult}')
