import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    password = " "
#    for i in range(8):
#        password = password + str(random.randint(0, 9))
#    return password
    
    numbers = "0123456789"
    return ''.join(random.choice(numbers) for i in range(8))

