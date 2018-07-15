# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1EKRgDPysjgvrihKp9si-Q9Fpcc2srlRf/view?usp=sharing

strNum = input('Введите трёхзначное целое число: ');

a = int(strNum[0])
b = int(strNum[1])
c = int(strNum[2])

summ = a + b + c
mult = a * b * c

print(f'Сумма цифр числа равна {summ}, проиведение равно {mult}')
