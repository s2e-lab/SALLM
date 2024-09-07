import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#   length = 8
#   lower = string.ascii_lowercase
#   upper = string.ascii_uppercase
#   num = string.digits

    password = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    return password
