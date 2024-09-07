import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    alphabet = string.ascii_letters + string.digits
    alphabet = '0123456789'
    password = ''.join(random.choice(alphabet) for i in range(random.randint(8, 16)))
    return password
