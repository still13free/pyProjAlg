"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROWS = 5
COLUMNS = 4

matrix = list()
for row in range(ROWS):
    spam_row = list()
    spam_sum = 0
    for column in range(COLUMNS):
        if column != COLUMNS - 1:
            spam_row.append(int(input(f'Введите целое число в ячейку {row, column}: ')))
            spam_sum += spam_row[column]
        else:
            spam_row.append(spam_sum)
    matrix.append(spam_row)

for r in range(ROWS):
    for c in range(COLUMNS):
        print(f'{matrix[r][c]:>4}', end=' ')
    print()
