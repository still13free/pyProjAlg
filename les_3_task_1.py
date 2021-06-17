"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

MIN_DIVIDEND = 2
MAX_DIVIDEND = 99
MIN_DIVISOR = 2
MAX_DIVISOR = 9

DIVIDENDS = [i for i in range(MIN_DIVIDEND, MAX_DIVIDEND + 1)]
DIVISORS = [j for j in range(MIN_DIVISOR, MAX_DIVISOR + 1)]

for divisor in DIVISORS:
    count = 0
    for dividend in DIVIDENDS:
        if dividend % divisor == 0:
            count += 1
    print(f'{count} чисел исходного диапазона кратны {divisor}')
