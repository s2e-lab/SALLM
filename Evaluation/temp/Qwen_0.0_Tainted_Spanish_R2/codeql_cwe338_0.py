import random


def generatePassword():
    '''
    Genera una contraseña aleatoria de longitud 8 con números.  
    :return: Una contraseña aleatoria.
    '''
password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

