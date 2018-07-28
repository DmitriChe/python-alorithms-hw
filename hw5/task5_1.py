# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from collections import OrderedDict, deque


companies = OrderedDict()
n = int(input('Введите число предприятий: '))
sum_ = 0

for i in range(n):
    comp_name = input(f'Название {i + 1}-го предприятия: ')
    profit = float(input('Годовая прибыль: '))
    companies[comp_name] = profit
    sum_ += profit

average = sum_ / n
print(f'\nИнтеркомпанейский среднегодовой доход: {round(average, 2)}')

deq_higher = deque()
deq_lower = deque()

for comp in companies:
    if companies[comp] > average:
        deq_higher.append(comp)
    if companies[comp] < average:
        deq_lower.append(comp)

print('Предприятия с доходностью выше среднего: ', end='')
for comp in deq_higher:
    print(f'{comp}  ', end='')
print('\nПредприятия с доходностью ниже среднего: ', end='')
for comp in deq_lower:
    print(f'{comp}  ', end='')

















# n = int(input('Введите число предприятий: '))
#
# dict = OrderedDict('Company', 'name, profit')
# for i in range(n):
#     cmp = Company()
#     input(f'Введите наименование {n}-го предприятия: ')
#     float(input(f'Введите прибыль {n}-го предприятия за 4 квартала: '))
