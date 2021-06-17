"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

from random import randint

MIN_VALUE = -100
MAX_VALUE = 100
AMOUNT = 15

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

max_negative = 0
for v in VALUES:
    if max_negative == 0 and v < 0 or max_negative < v < 0:
        max_negative = v
if max_negative < 0:
    print(f'Максимальный отрицательный элемент {max_negative} в позиции {VALUES.index(max_negative)}')
else:
    print('Отрицательных элементов нет')
