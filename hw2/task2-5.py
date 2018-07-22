# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

first = 32
last = 127
pairs_str = ''

for i in range(first, last+1):

    if (i - first) % 10 == 0 and i > first:
        print(pairs_str)
        pairs_str = ''
    if i > 99:
        pairs_str += f'{chr(i)} - {ord(chr(i))}  '
    else:
        pairs_str += f'{chr(i)} - {ord(chr(i))}   '

print(pairs_str)
