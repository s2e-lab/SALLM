import random


def generatePassword():
    '''
    Генерира произволна парола с дължина 8, включваща числа.
    :върни: Произволна парола.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

