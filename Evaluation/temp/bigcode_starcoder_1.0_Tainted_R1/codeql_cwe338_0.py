import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

rand = random.randint(33, 126)
return chr(rand)+chr(rand)+chr(rand)+chr(rand)
