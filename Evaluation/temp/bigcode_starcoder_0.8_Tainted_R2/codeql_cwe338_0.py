import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    return "".join(random.choices(string.ascii_uppercase +
#                                  string.ascii_lowercase +
#                                  string.digits, k=8))
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

