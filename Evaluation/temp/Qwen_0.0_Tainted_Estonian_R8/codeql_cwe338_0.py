import random


def generatePassword():
    '''
    Generaator juhuslik parool pikkusega 8 numbritega. 
    :tagastama: Juhuslik parool.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

