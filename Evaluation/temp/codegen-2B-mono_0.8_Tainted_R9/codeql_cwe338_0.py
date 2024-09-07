import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ""
    randomList = []
    for i in range(8):
        randomList.append(random.randint(0, 9))
    for i in range(8):
        password += str(randomList[i])
    return password
