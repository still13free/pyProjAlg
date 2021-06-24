"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

MIN_VALUE = -100
MAX_VALUE = 100
AMOUNT = 15

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

i_min_1, i_min_2 = 0, 0  # i_min_1 <= i_min_2
for i, v in enumerate(VALUES):
    if v <= VALUES[i_min_1]:
        i_min_2 = i_min_1
        i_min_1 = i
    elif v <= VALUES[i_min_2] or i_min_1 == i_min_2:
        i_min_2 = i
print(VALUES[i_min_1], VALUES[i_min_2])
