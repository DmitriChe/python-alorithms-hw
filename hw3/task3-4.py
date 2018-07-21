# 4. Определить, какое число в массиве встречается чаще всего.
import random

arr = sorted([random.randint(0, 100) for _ in range(100)])
print(arr)

max_count = 0
count = 1
most_frequent_nums = []

for i in range(len(arr) - 1):

    if arr[i] == arr[i + 1]:
        count += 1

    else:
        if count == max_count:
            most_frequent_nums.append(arr[i])
        if count > max_count:
            max_count = count;
            most_frequent_nums = [arr[i]]

        count = 1

print(f'Список чисел с максимальной частотностью ({max_count}) : {most_frequent_nums}')

# проверка
print('\nПроверка:')
arr_set = list(set(arr))
for item in arr_set:
    print(f'{item} : {arr.count(item)}')
