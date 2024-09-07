import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

	# generate a random integer of length 8
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))