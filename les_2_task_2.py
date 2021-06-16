"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

BASE = 10

while True:
    number = int(input('Введите натуральное число: '))
    if number > 0:
        even, odd = 0, 0
        while number > 0:
            if (number % BASE) % 2:
                odd += 1
            else:
                even += 1
            number //= BASE
        print(f'\tЧётных цифр: {even}\n\tНечётных цифр: {odd}\n')
    else:
        break
