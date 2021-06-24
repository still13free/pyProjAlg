"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

MIN_VALUE = -10
MAX_VALUE = 10

ROWS = 5
COLUMNS = 4

matrix = list()
for row in range(ROWS):
    spam_row = list()
    for column in range(COLUMNS):
        spam_row.append(randint(MIN_VALUE, MAX_VALUE))
    matrix.append(spam_row)

for r in range(ROWS):
    for c in range(COLUMNS):
        print(f'{matrix[r][c]:>4}', end='')
    print()

max_of_min_col = 0
for c in range(COLUMNS):
    spam_min = matrix[0][c]
    for r in range(ROWS):
        spam_el = matrix[r][c]
        if spam_el < spam_min:
            spam_min = spam_el
    print(f'Минимальный элемент столбца {c}: {spam_min}')
    if c == 0 or spam_min > max_of_min_col:
        max_of_min_col = spam_min
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min_col}')
