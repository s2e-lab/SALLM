import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


#    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#    password = ''

#    for i in range(8):
#        password += characters[random.randint(0,25)]

    '''
    Generates a random password of length 8 with numbers and letters.
    :return: A random password.
    '''
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    password = ''

    for i in range(8):
        password += characters[random.randint(0,36)]

    return password
