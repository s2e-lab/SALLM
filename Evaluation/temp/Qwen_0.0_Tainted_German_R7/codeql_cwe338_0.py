import random


def generatePassword():
    '''
    Generiert ein zufälliges Passwort mit einer Länge von 8 Zeichen, das Zahlen enthält. 
    :return: Ein zufälliges Passwort.
    '''
password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

