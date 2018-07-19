# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# https://drive.google.com/file/d/1HCcC31zqIFivCZvIUxD6Z4EAvuPlSXZ_/view?usp=sharing

letter_shift = ord('a') - 1

l1 = input('Введите первую букву латинского алфавита в НИЖНЕМ регистре: ')
l2 = input('Введите вторую букву латинского алфавита в НИЖНЕМ регистре: ')

if l1 == l2:
    print('Неверный ввод! Введена одна и та же буква!')
else:
    place_l1 = ord(l1) - letter_shift;
    place_l2 = ord(l2) - letter_shift;
    delta = abs(place_l1 - place_l2) - 1;
    print(f'Позиция буквы {l1}: {place_l1}')
    print(f'Позиция буквы {l2}: {place_l2}')
    print(f'Между ними букв: {delta}')
