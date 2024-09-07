import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Length of the password
    length = 8
    # Generate a random password
    randomSource = string.ascii_letters + string.digits
    password = ''.join(random.sample(randomSource, length))
    return password

