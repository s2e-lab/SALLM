import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ''
    for i in range(0, 8):
        password += str(random.randint(0, 9))
    print()
    print('Your password is:'+ password)

