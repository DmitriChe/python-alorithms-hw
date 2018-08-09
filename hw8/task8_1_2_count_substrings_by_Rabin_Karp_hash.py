# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib.
import hashlib


def subs_count_by_rabin_karp(s):
    count = 0
    h_subs_list = []

    for subs_len in range(1, len(s) + 1):  # длина подстроки
        print(f'Длина подстроки {subs_len} симв.:')
        for i in range(0, len(s) + 1 - subs_len):  # берем очередную подстроку, длиной subs_len
            subs = s[i: i + subs_len]
            h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
            if not(h_subs in h_subs_list):

                print(f'{subs}')
                h_subs_list.append(h_subs)
                count += 1

    print(f'\nМассив хэшей:')
    for item in h_subs_list:
        print(item)
    return count


print('Подсчет числа подстрок в строке на базе алгоритма Рабина-Карпа')
s = input('Введите строку: ')

print(f'Длина строки: {len(s)}\n')
print(f'\nЧисло вхождений подстроки: {subs_count_by_rabin_karp(s)}')
