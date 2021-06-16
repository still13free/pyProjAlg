"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

BASE = 10


def sum_of_num(number: int) -> int:
    sum_num = 0
    while number > 0:
        sum_num += number % BASE
        number //= BASE
    return sum_num


max_num = 0
max_sum = 0

while True:
    num = int(input('Введите натуральное число: '))
    if num > 0:
        num_sum = sum_of_num(num)
        if num_sum > max_sum:
            max_num = num
            max_sum = num_sum
    else:
        print(f'Наибольшее число {max_num} с суммой цифр {max_sum}')
        break
