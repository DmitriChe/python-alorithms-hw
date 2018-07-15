# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1DB2n6CsHQWO5vFCdfyQSaMe0aVehKo4O/view?usp=sharing

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a != b and b != c and c != a:
    if (a > b and a < c) or (a < b and a > c):
        print(f'Среднее число: {a}')
    elif (b > a and b < c) or (b < a and b > c):
        print(f'Среднее число: {b}')
    else:
        print(f'Среднее число: {c}')
else:
    print('Среднего числа нет!')
