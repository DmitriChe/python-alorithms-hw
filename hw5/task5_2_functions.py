# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def reverse_list(lst):
    rev = []
    for i in range(len(lst) - 1, -1, -1):
        rev += lst[i]
    return rev


def list_to_string(lst):
    s = ''
    for i in range(len(lst)):
        s += lst[i]
    return s


def wrong_hex(hex_lst):
    hex_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for item in hex_lst:
        if item in hex_symbols:
            continue
        else:
            print(f'ОШИБКА ВВОДА: цифра {item} не щестнадцатиричная!')
            return True
    return False


def hex_to_dec(hex_lst):
    base = 16
    dec = 0
    trans_hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    for i in range(len(hex_lst)):
        dec += trans_hex_dict[hex_lst[i]] * base ** i
    return dec


def dec_to_hex(dec):
    base = 16
    trans_dec_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }
    hex_list = []
    while dec > 0:
        hex_list += [trans_dec_dict[dec % base]]
        dec //= base
    return hex_list


while True:
    stop = False

    # Ввод и проверка первого числа
    hex1 = list(input('Введите первое шестнадцатиричное число: ').lower())
    if wrong_hex(hex1):
        break

    # Ввод и проверка второго числа
    hex2 = list(input('Введите второе шестнадцатиричное число: ').lower())
    if wrong_hex(hex2):
        break

    print(f'Массив первого числа: {hex1}\nМассив втого числа: {hex2}')

    # реверс hex чисел для удобства вычисления
    hex1_rev = reverse_list(hex1)
    hex2_rev = reverse_list(hex2)

    # перевод в 10x систему
    dec1 = hex_to_dec(hex1_rev)
    dec2 = hex_to_dec(hex2_rev)
    print(f'В DEC СИСТЕМЕ:\nпервое число: {dec1}\nвторое число: {dec2}')

    # расчет десятичных суммы и произведения
    sum_dec = dec1 + dec2
    mult_dec = dec1 * dec2
    print(f'сумма: {sum_dec}\nпроизведение: {mult_dec}')

    # первод суммы и произведения в hex
    sum_hex = reverse_list(dec_to_hex(sum_dec))
    mult_hex = reverse_list(dec_to_hex(mult_dec))

    # вывод суммы и произведения hex
    print(f'В HEX СИСТЕМЕ:\nсумма: {list_to_string(sum_hex)}')
    print(f'произведение: {list_to_string(mult_hex)}')

    new_try = input('Хотите выйти? [y - выйти, any key - продолжить]: ')
    if new_try == 'y':
        break
