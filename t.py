
def is_valid(n):
    if n.isdigit():
        if  left < n < rigth:
            return True
    return False

import random
left = 1
rigth = 100
num = random.randint(left,rigth)
print('Добро пожаловать в числовую угадайку')

while True:
    n = input()
    if is_valid(n) == False:
       print('А может быть все-таки введем целое число от 1 до 100?')
    n =int(n)
    if num > n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif  num < n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif num == n:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
