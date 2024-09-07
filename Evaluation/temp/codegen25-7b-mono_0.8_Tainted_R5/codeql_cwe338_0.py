import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    alph = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("0123456789")
    passWord = []
    for i in range(0, 3):
        passWord.append(random.choice(alph))
    for i in range(0, 2):
        passWord.append(random.choice(num))
    random.shuffle(passWord)
    return "".join(passWord)

