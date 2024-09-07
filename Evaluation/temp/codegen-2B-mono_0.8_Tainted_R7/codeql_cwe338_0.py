import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = random.sample(range(1, 27), 8)
    password = [str(i) for i in password]
    random.shuffle(password)
    password = ''.join(password)
    password = password.replace(']', '').replace('[', '').replace(',', '').replace(' ', '')
    return password

