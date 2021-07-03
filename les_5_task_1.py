"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

DELIMITER = '=============================='

companies = defaultdict(list)
amount = int(input('Введите количество предприятий: '))
for i in range(1, amount + 1):
    print(DELIMITER)
    name = input(f'Введите наименование {i}-го предприятия: ')
    sum_profit = 0
    for j in range(1, 5):
        profit = round(float(input(f'\tПрибыль за {j}-ый квартал: ')), 2)
        companies[name].append(profit)
        sum_profit += profit
    companies[name].append(sum_profit)

average_profit = 0
for profits in companies.values():
    average_profit += profits[4]  # в 4-ую ячейку мы заранее посчитали суммарную прибыль предприятия за год
average_profit = round(average_profit / amount, 2)
print(DELIMITER, f'Средняя прибыль предприятий за год = {average_profit}', sep='\n')

print(DELIMITER, f'Список предприятий, чья прибыль выше среднего:', sep='\n')
for name, profits in companies.items():
    if profits[4] >= average_profit:
        print('\t', name)

print(DELIMITER, f'Список предприятий, чья прибыль ниже среднего:', sep='\n')
for name, profits in companies.items():
    if profits[4] < average_profit:
        print('\t', name)
print(DELIMITER)
