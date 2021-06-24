"""
Задание 2.4
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

from timeit import timeit
from cProfile import run


def test(func):
    list_ = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625, 0.66796875, 0.666015625]
    for i, item in enumerate(list_):
        assert item == func(i + 1), f'Error {i + 1}'
    print('Test OK')


# Вариант 1 (сданный, скорректированный для этой практики)
def get_row_sum_1(n: int, x=-0.5, i=0, row_sum=0) -> float:
    while i < n:
        row_sum += x ** i
        i += 1
    return row_sum


# Вариант 2 (геометрическая прогрессия)
def get_row_sum_2(n: int, x=-0.5) -> float:
    return 1 * (1 - x ** n) / (1 - x)


# Вариант 3 (рекурсия)
def get_row_sum_3(n, start=1.0, step=-0.5):
    if n == 1:
        return start
    return start + get_row_sum_3(n - 1, start * step)


# Вариант 4 (рекурсия с ограничением)
def get_row_sum_4(n, start=1.0, step=-0.5):
    if n == 1:
        return start
    if n > 55:
        return 2 / 3
    return start + get_row_sum_3(n - 1, start * step)


# test(get_row_sum_1)
# test(get_row_sum_2)
# test(get_row_sum_3)
# test(get_row_sum_4)

# for r in range(1, 6):
#     out = timeit(f'get_row_sum_1({r*25})', number=1000, globals=globals())
#     print(f'{r * 25}\t{out:.5f}')
# print()
# for r in range(1, 6):
#     out = timeit(f'get_row_sum_2({r*25})', number=1000, globals=globals())
#     print(f'{r * 25}\t{out:.5f}')
# print()
# for r in range(1, 6):
#     out = timeit(f'get_row_sum_3({r*25})', number=1000, globals=globals())
#     print(f'{r * 25}\t{out:.5f}')
# print()
# for r in range(1, 6):
#     out = timeit(f'get_row_sum_4({r*25})', number=1000, globals=globals())
#     print(f'{r * 25}\t{out:.5f}')

# run('get_row_sum_1(990)')
# run('get_row_sum_2(990)')
# run('get_row_sum_3(990)')
# run('get_row_sum_4(990)')

"""
    Функция 1   Функция 2   Функция 3   Функция 4
25	0.00909     0.00059     0.00658     0.00672 
50	0.01864     0.00074     0.01395     0.01408
75	0.02771     0.00061     0.02181     0.00022
100	0.03633     0.00060     0.02907     0.00023
125	0.04533     0.00060     0.03951     0.00023

На приложенных графиках хорошо заметна линейная зависимость 1-ой и 3-ей функции
В то же время функция 2 наиболее стабильна, поскольку не зависит от n
Функция 4 же изначально сравнима по затратам с 1-ой и 3-ей,
однако при n > 55 становится даже менее затратна, чем функция 2

         4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 practice.py:19(get_row_sum_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 practice.py:27(get_row_sum_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         993 function calls (4 primitive calls) in 0.003 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    990/1    0.002    0.000    0.002    0.002 practice.py:32(get_row_sum_3)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 practice.py:39(get_row_sum_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Я искренне пытался добиться не нулей, но решил уже не менять в очередной раз задачу
Можно заметить, что чем ближе третий вариант (с рекурсией без ограничения) к своему пределу (глубина рекурсии),
тем больше времезатратной становится функция, чего нет у аналогичных

Несмотря на затратность функции 1, она способна работать при n > 1000, на что неспособна функция 3 (ввиду рекурсии)
Хотя функция 4 при n > 55 работает быстрее функции 2 (ввиду меньшего количества вычислений),
отдать предпочтение имеет смысл именно последней,
поскольку независимость от числа n позволяет ей отрабатывает быстро всегда
"""
