"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
 - алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
 - постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
   Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint


def smart_bubble_sort(array: list, n=1):
    len_array = len(array)
    while n < len_array:
        is_changed = False
        for i in range(len_array - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True
        if is_changed:
            n += 1
        else:
            break
    return n  # возвращаем количество проходов


MIN_VALUE = -100
MAX_VALUE = 100
AMOUNT = 10
VALUES = [randint(MIN_VALUE, MAX_VALUE - 1) for _ in range(AMOUNT)]

print(VALUES)
count = smart_bubble_sort(VALUES)
print('Количество проходов:', count)
print(VALUES)
