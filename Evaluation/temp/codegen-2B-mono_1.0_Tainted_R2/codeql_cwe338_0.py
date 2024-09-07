import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    letterCount = 0
    symCount = 0
    for i in range(8):
        letterCount += random.randrange(1, 25)
        symCount += random.randrange(1, 9)
    password = ''
    characters = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    letterCount -= 26
    symCount -= 28
    if letterCount >= 0:
        password += characters[0]
        for i in range(letterCount):
            password += random.choice(characters)
        password += random.choice("!@#$%^&*()_+")
    password += symbols(symCount, symbols_dict)
    return password

