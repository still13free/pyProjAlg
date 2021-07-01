"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

from random import randint


def find_median(array: list):
    if len(array) == 1:
        return array[0]

    for el_1 in array:
        spam = {'less': 0, 'more': 0, 'equal': 0}
        for el_2 in array:
            if el_2 < el_1:
                spam['less'] += 1
            elif el_2 > el_1:
                spam['more'] += 1
            else:
                spam['equal'] += 1
        if spam['less'] == spam['more'] or 0 <= len(array) // 2 - spam['less'] < spam['equal']:
            return el_1

    return None


MIN_VALUE = -5
MAX_VALUE = 5
AMOUNT = 5
VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(2 * AMOUNT + 1)]

print(VALUES)
print(find_median(VALUES))
VALUES.sort()
print(VALUES)
