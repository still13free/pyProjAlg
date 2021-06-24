"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""


def test(func):
    list_ = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(list_):
        assert item == func(i + 1), f'Error {i + 1}'
    print('Test OK')


# решето Эратосфена, выводит ВСЕ простые числа до n
# нужно переписать
def sieve(n: int) -> int:
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m + m
            while j < n:
                a[j] = 0
                j += m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    print(b)
    return n


primes = []


def prime(n: int, start=2) -> int:
    while len(primes) < n:
        for div in primes:
            if start % div == 0:
                break
        else:
            primes.append(start)
        start += 1
    return primes[n - 1]


test(prime)
