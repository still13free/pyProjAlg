"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

symbol_1 = input('Введите первую строчную букву: ')
symbol_2 = input('Введите вторую строчную букву: ')
if symbol_1 != symbol_2:
    number_1 = ord(symbol_1) - ord('a') + 1
    number_2 = ord(symbol_2) - ord('a') + 1
    symbols_between = abs(number_1 - number_2) - 1
    print(f'Порядковый номер {symbol_1} — {number_1}')
    print(f'Порядковый номер {symbol_2} — {number_2}')
    print(f'Количество символов между {symbol_1} и {symbol_2} — {symbols_between}')
else:
    print('Вы ввели одинаковые буквы')
