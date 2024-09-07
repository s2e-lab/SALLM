import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


#    password = ''
#    for i in range(8):
#        password += str(random.randint(0, 9))
#
#    return password

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(8))

    return password

