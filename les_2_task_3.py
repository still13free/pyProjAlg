"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

BASE = 10

while True:
    number = int(input('Введите натуральное число: '))
    if number > 0:
        reverse = 0
        while number > 0:
            reverse = reverse * BASE + number % BASE
            number //= BASE
        print(f'Обратное число: {reverse}\n')
    else:
        break
