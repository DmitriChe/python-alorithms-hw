# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# https://drive.google.com/file/d/1a_oV2COwiUasRauR9jA7VMWhjJcX8HV2/view?usp=sharing

y = int(input('Введите год для проверки висоскосности в формате yyyy: '))

if y % 400 == 0:
    print(f'{y} год - високосный')
elif y % 100 != 0:
    if y % 4 == 0:
        print(f'{y} год - високосный')
    else:
        print(f'{y} год - невисокосный')
else:
    print(f'{y} год - невисокосный')
