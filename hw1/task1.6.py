# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/17tp9jWJEAT3PrLxcQffRJcAzwGHJfSka/view?usp=sharing

letter_shift = ord('a') - 1

letter_pos = int(input('Введите порядковый номер буквы в латинском алфавите: '))

if letter_pos < 1 or letter_pos > 26:
    print('Неверный ввод! В латинском алфавите всего 26 букв!')
else:
    letter = chr(letter_pos + letter_shift)
    print(f'{letter_pos}-я буква это: {letter}')