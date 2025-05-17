import random


def generatePassword():
    '''
    Véletlenszerű jelszót generál 8 karakter hosszúságú, számokkal.
    :visszatér: Egy véletlenszerű jelszó.
    '''
orical
    password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

