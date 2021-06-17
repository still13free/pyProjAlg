"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

MIN_VALUE = 0
MAX_VALUE = 100
AMOUNT = 10

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

values_even_numbers_indexes = []
for i, v in enumerate(VALUES):
    if v % 2 == 0:
        values_even_numbers_indexes.append(i)
print(values_even_numbers_indexes)
