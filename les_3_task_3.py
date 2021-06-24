"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

MIN_VALUE = -150
MAX_VALUE = 150
AMOUNT = 15

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

# попробуем обойти запрет индексами, хотя вангую, что не прокатит
i_max, i_min = 0, 0
for i, v in enumerate(VALUES):
    if v > VALUES[i_max]:
        i_max = i
    if v < VALUES[i_min]:
        i_min = i
VALUES[i_min], VALUES[i_max] = VALUES[i_max], VALUES[i_min]
print(VALUES)

# а вообще мозг ломается в противоречии: найти min и max, не используя функции (это понятно) и их аналоги
# в любом случае придётся как-то искать или сами значения, или их индексы — то есть пользоваться аналогами
