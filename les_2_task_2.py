"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

BASE = 10


def count_even_and_odd_numbers(number: int) -> (int, int):
    even, odd = 0, 0
    while number > 0:
        if (number % BASE) % 2:
            odd += 1
        else:
            even += 1
        number = number // BASE
    return even, odd


while True:
    num = int(input('Введите натуральное число: '))
    if num > 0:
        e, o = count_even_and_odd_numbers(num)
        print(f'\tЧётных цифр: {e}\n\tНечётных цифр: {o}\n')
    else:
        break
