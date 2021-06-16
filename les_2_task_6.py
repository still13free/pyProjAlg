"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""

from random import randint

BEGIN = 0
END = 100
TRIES = 10

win = False
secret = randint(BEGIN, END)
# print(secret)
print('ИГРА "УГАДАЙ ЧИСЛО!"')
for trying in range(TRIES):
    number = int(input(f'Попытка №{trying + 1}. Ваш ответ: '))
    if number < secret:
        print("Загаданное число больше")
    elif number > secret:
        print("Загаданное число меньше")
    else:
        win = True
        break

if win:
    print(f"Какая интуиция! Да, мы загадали число {secret}!")
else:
    print(f"К сожалению, Вам не удалось угадать число {secret}!")
