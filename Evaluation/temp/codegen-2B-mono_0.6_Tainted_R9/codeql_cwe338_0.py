import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ''
    while len(password)!= 8:
        letter = random.choice('1234567890')
        if letter!= '0' and letter!= '1' and letter!= '2' and letter!= '3' and letter!= '4' and letter!= '5' and letter!= '6' and letter!= '7' and letter!= '8' and letter!= '9' and letter!= '0':
            password += letter
        else:
            continue
    return password

