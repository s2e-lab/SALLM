import random


def generatePassword():
    '''
    Gera uma senha aleatória de comprimento 8 com números.  
    :retorno: Uma senha aleatória.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

