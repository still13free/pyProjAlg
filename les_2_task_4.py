"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

X = -0.5

while True:
    number = int(input('Введите натуральное число: '))
    if number > 0:
        i, row_sum = 0, 0
        while i < number:
            row_sum += X ** i
            i += 1
        print(f'Сумма {number} элементов ряда: {row_sum}\n')
    else:
        break
