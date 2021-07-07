"""
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def find_all_subs(string: str):
    length = len(string)
    subs = []
    for i in range(length):
        for j in range(i+1, length+1):
            spam_sub = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            if spam_sub not in subs:
                subs.append(spam_sub)
    return len(subs)


while True:
    s = input('Введите строку для поиска подстрок: ')
    if s == '':
        break
    print('Количество подстрок', find_all_subs(s), '\n')
