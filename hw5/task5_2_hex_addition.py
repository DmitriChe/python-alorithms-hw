# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


def wrong_hex(hex_lst):
    hex_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for item in hex_lst:
        if item in hex_symbols:
            continue
        else:
            print(f'ОШИБКА ВВОДА: цифра {item} не щестнадцатиричная!')
            return True
    return False


def reverse_list(lst):
    rev = []
    for i in range(len(lst) - 1, -1, -1):
        rev += lst[i]
    return rev


def make_equal_length(lst1, lst2):
    delta_len = abs(len(lst1) - len(lst2))

    if len(lst1) > len(lst2):
        for _ in range(delta_len):
            lst2 += ['0']
    elif len(lst1) < len(lst2):
        for _ in range(delta_len):
            lst1 += ['0']
    return lst1, lst2


def hex_addition(lst1, lst2):
    max_len = max(len(lst1), len(lst2))
    sum_hex = []
    appendix = 0
    for i in range(max_len):
        dig1 = hex_to_dec(lst1[i])
        dig2 = hex_to_dec(lst2[i])
        dig_sum = (dig1 + dig2 + appendix)
        if dig_sum > 15:
            appendix = 1
            sum_hex += dec_to_hex(dig_sum - 16)
        else:
            appendix = 0
            sum_hex += dec_to_hex(dig_sum)
        if i == max_len - 1 and appendix > 0:
            sum_hex += str(appendix)

    return sum_hex


def hex_to_dec(key):

    hextodec_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    return hextodec_dict[key]


def dec_to_hex(key):

    dectohex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }

    return dectohex_dict[key]


def list_to_string(lst):
    s = ''
    for i in range(len(lst)):
        s += lst[i]
    return s


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

    print(f'{hex1} - массив первого числа\n{hex2} - массив втого числа')

    # реверс hex чисел для удобства вычисления
    hex1_rev = reverse_list(hex1)
    hex2_rev = reverse_list(hex2)

    # уравнивание чисел по длине нулями:
    hex1_rev, hex2_rev = make_equal_length(hex1_rev, hex2_rev)
    print(f'Проверка выравнивания:\n{hex1_rev} - реверс первого числа: \n{hex2_rev} - реверс втого числа: ')

    # сложение hex, реверс и вывод
    sum_hex_rev = hex_addition(hex1_rev, hex2_rev)
    sum_hex = reverse_list(sum_hex_rev)
    print(f'Массив суммы:\n{sum_hex}')

    # произведение hex, реверс и вывод
    # mult_hex_rev = hex_multiply(hex1_rev, hex2_rev)
    # mult_hex = reverse_list(mult_hex_rev)
    # print(f'Массив суммы:\n{sum_hex}')

    # вывод суммы и произведения hex
    print(f'\nсумма: {list_to_string(sum_hex)}')
    # print(f'произведение: {list_to_string(mult_hex)}')

    new_try = input('Хотите выйти? [y - выйти, any key - продолжить]: ')
    if new_try == 'y':
        break
