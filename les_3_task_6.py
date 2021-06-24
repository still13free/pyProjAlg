"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

MIN_VALUE = -100
MAX_VALUE = 100
AMOUNT = 15

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

i_max, i_min = 0, 0
for i, v in enumerate(VALUES):
    if v > VALUES[i_max]:
        i_max = i
    if v < VALUES[i_min]:
        i_min = i

sum_el = 0
start, end = (i_min, i_max) if i_min < i_max else (i_max, i_min)
for i in range(start + 1, end):
    sum_el += VALUES[i]
print(f'Сумма элементов массива между {start} и {end} элементами: {sum_el}')
