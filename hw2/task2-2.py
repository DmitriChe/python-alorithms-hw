# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1VRYXC5E9JAo-B7kXaRiGJb4CNuZdRe5K/view?usp=sharing

num = int(input('Введите натуральное число: '))

odd = even = 0

while num > 0:
    if num % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10
print(f'Четных цифр: {even}, нечетных: {odd}')
