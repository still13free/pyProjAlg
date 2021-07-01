"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform


def merge_sort(array):
    len_array = len(array)
    if len_array == 1 or len_array == 0:
        return

    middle = len_array // 2
    left, right = array[:middle], array[middle:]
    merge_sort(left)
    merge_sort(right)

    spam, il, ir = [], 0, 0
    while il < len(left) and ir < len(right):
        if left[il] <= right[ir]:
            spam.append(left[il])
            il += 1
        else:
            spam.append(right[ir])
            ir += 1
    while il < len(left):
        spam.append(left[il])
        il += 1
    while ir < len(right):
        spam.append(right[ir])
        ir += 1
    for i in range(len_array):
        array[i] = spam[i]


MIN_VALUE = 0
MAX_VALUE = 50
AMOUNT = 10
POWER = 3
VALUES = [round(uniform(MIN_VALUE, MAX_VALUE - (0.1**POWER)), POWER) for _ in range(AMOUNT)]

print(VALUES)
merge_sort(VALUES)
print(VALUES)
