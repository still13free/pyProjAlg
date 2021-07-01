import sys


def get_mem(obj, memory=0):
    for i in obj:
        memory += sys.getsizeof(i)
    return memory


number = input('Введите натуральное число: ')
number = list(number)
count = len(number)
reverse = [number[count - 1 - i] for i in range(count)]
print(reverse)

sum_mem = sys.getsizeof(number) + get_mem(number) + sys.getsizeof(reverse) + get_mem(reverse) + sys.getsizeof(count)
print(f'Занимаемой памяти в байтах: {sum_mem}')


"""
Рассматриваем number = str(sys.maxsize)
['9', '2', '2', '3', '3', '7', '2', '0', '3', '6', '8', '5', '4', '7', '7', '5', '8', '0', '7']
['7', '0', '8', '5', '7', '7', '4', '5', '8', '6', '3', '0', '2', '7', '3', '3', '2', '2', '9']
Занимаемой памяти в байтах: 2392
Занимаемой памяти в байтах: 2316 (reverse = number[::-1] и исключить переменную count)

Не будем заморачиваться над тем, чтобы красиво вывести развёрнутое число —
в данном варианте и так беда с заниманием кучи ненужной памяти
Соответственно, по использованию памяти предпочтение отдаётся первой программе
"""