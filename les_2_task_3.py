"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

BASE = 10


def reverse_number(number: int) -> int:
    reverse = 0
    while number > 0:
        reverse = reverse * BASE + number % BASE
        number //= BASE
    return reverse


while True:
    num = int(input('Введите натуральное число: '))
    if num > 0:
        print(f'Обратное число: {reverse_number(num)}\n')
    else:
        break
