import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    password = ""
#    for i in range(8):
#        password += random.choice(string.ascii_letters + string.digits)
#    return password
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

