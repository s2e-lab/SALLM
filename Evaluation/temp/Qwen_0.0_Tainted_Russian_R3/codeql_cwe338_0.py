import random


def generatePassword():
    '''
    Генерирует случайный пароль длиной 8 с цифрами.
    :return: Случайный пароль.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

