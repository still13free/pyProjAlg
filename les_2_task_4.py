"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def get_row_sum(n: int, x=1) -> int:
    row_sum, i = 0, 0
    while i < n:
        row_sum += x
        i += 1
        x *= -0.5
    return row_sum


while True:
    num = int(input('Введите натуральное число: '))
    if num > 0:
        print(f'Сумма {num} элементов ряда: {get_row_sum(num)}\n')
    else:
        break
