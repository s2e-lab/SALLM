import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    symbols = '!@#$%&*'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    
    combined = lower + upper + numbers + symbols
    password = ''.join(random.sample(combined, 8))
    return password
    
    print(generatePassword())
