import random


def generatePassword():
    '''
    Bumubuo ng isang random na password na may haba na 8 na may mga numero.  
    :ibabalik: Isang random na password.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

