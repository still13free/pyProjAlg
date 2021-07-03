"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque
from functools import reduce


def addition(a: deque, b: deque, surplus=0) -> deque:
    if len(a) >= len(b):
        longer, shorter = a, b
    else:
        longer, shorter = b, a
    min_num_of_additions = len(shorter)
    all_num_of_additions = len(longer)

    result = deque()
    for i in range(all_num_of_additions):
        if i < min_num_of_additions:
            # берём hex-цифры
            n1 = shorter[min_num_of_additions - 1 - i]
            n2 = longer[all_num_of_additions - 1 - i]
            # получаем их dec-значения
            n1 = allowed_numbers.index(n1)
            n2 = allowed_numbers.index(n2)
            n = n1 + n2 + surplus  # складываем, добавляем излишек предыдущего разряда
        else:
            n = longer[all_num_of_additions - 1 - i]
            n = allowed_numbers.index(n)
            n += surplus
        surplus = n // BASE  # определяем излишек текущего разряда
        n -= surplus * BASE
        n = allowed_numbers[n]  # определяем цифру hex
        result.appendleft(n)
    if surplus != 0:
        result.appendleft(str(surplus))
    return result


def multiplication(a: deque, b: deque, surplus=0) -> deque:
    a_digits = len(a)
    b_digits = len(b)
    pre_result = []
    for i in range(a_digits):
        spam = deque()
        for j in range(b_digits):
            na = a[a_digits - 1 - i]
            nb = b[b_digits - 1 - j]
            na = allowed_numbers.index(na)
            nb = allowed_numbers.index(nb)
            n = na * nb + surplus
            surplus = n // BASE
            n -= surplus * BASE
            n = allowed_numbers[n]
            spam.appendleft(n)
        if surplus != 0:
            spam.appendleft(allowed_numbers[surplus])
            surplus = 0
        for k in range(i):
            spam.append('0')
        pre_result.append(spam)
    return reduce(addition, pre_result)


# делаем красивый вывод
def deque_to_str(a: deque) -> str:
    result = ''
    for s in a:
        result += s
    return result


def test_deque(a: deque) -> bool:
    for s in a:
        if s not in allowed_numbers:
            return False
    return True


BASE = int(input('Введите базис счётной системы: '))
if BASE <= 10:
    allowed_numbers = [chr(i + 48) for i in range(BASE)]
else:
    allowed_numbers = [chr(i + 48) for i in range(10)]
    allowed_numbers.extend([chr(i + 65) for i in range(BASE - 10)])
print(f'Разрешённый набор цифр: {allowed_numbers}')

while True:
    decision = input("\nНажмите Enter, чтобы продолжить (любой символ - выход)")
    if decision != '':
        break
    else:
        first = deque(input(f'Введите первое число {BASE}-ой системы: ').upper())
        second = deque(input(f'Введите второе число {BASE}-ой системы: ').upper())
        if not (test_deque(first) and test_deque(second)):
            print('WARNING: Как минимум одно число введено некорректно')
            print(f'Разрешённый набор цифр: {allowed_numbers}')
            continue
        add = addition(first, second)
        mul = multiplication(first, second)
        print(f'Результат сложения: {deque_to_str(add)}')
        print(f'Результат умножения: {deque_to_str(mul)}')
