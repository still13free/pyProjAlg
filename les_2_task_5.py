"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

BEGIN = 32
END = 127
PER_ROW = 10

for i, num in enumerate(range(BEGIN, END + 1)):
    if not i % PER_ROW:
        print()
    print(f'{num}:"{chr(num)}"', end='\t\t')
