"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

MIN_VALUE = -10
MAX_VALUE = 10
AMOUNT = 25

VALUES = [randint(MIN_VALUE, MAX_VALUE) for _ in range(AMOUNT)]
print(VALUES)

max_freq_item = VALUES[0]
max_freq_count = 0
for v in VALUES:
    spam_freq = VALUES.count(v)
    if max_freq_count < spam_freq:
        max_freq_count = spam_freq
        max_freq_item = v
print(f'Чаще всего в массиве встречается число {max_freq_item}, повторений: {max_freq_count}')
