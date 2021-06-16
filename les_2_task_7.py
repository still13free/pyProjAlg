"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def seq_n(n: int) -> int:
    if n > 0:
        # print(f'{n} + ', end='')
        return n + seq_n(n - 1)
    # print(n)
    return 0


num = int(input('Введите натуральное число: '))
if num > 0:
    left = seq_n(num)
    right = num * (num + 1) // 2
    print(f'1+2+...+n = n(n+1)/2 is {left == right}')


"""
оригинальная версия с тестирование через бесконечный цикл

def qed(n: int) -> (int, int):  # quod erat demonstrandum
    left, right = 0, 0
    for i in range(n):
        left += i + 1
    right = n * (n + 1) // 2
    return left, right


while True:
    num = int(input('Введите натуральное число: '))
    if num > 0:
        fst, snd = qed(num)
        print(f'1+2+...+n = n(n+1)/2 is {fst == snd}')
    else:
        break
"""
