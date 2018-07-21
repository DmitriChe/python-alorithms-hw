# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

count = [0] * 8
for num in range(2, 100):
    for divider in range(2, 10):
        if num % divider == 0:
            count[divider - 2] += 1

            # print(f'{num} кратно {divider}')  # раскомментировать для проверки

for divider in range(2, 10):
    print(f'Количество чисел, кратных {divider} суть {count[divider - 2]}')