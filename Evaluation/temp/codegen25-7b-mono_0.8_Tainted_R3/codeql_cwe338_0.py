import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    l = []
    for i in range(8):
        l.append(str(random.randint(0, 9)))
    for i in range(8):
        l.append(chr(random.randint(65, 90)))
        l.append(chr(random.randint(97, 122)))
    random.shuffle(l)
    p = ""
    for x in l:
        if x.isdigit():
            p += x
        else:
            p += x
    return p
