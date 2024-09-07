import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


#    password = ''
#    for i in range(0, 8):
#        password += str(random.randint(0, 9))

    password = str(random.randint(0, 9))
    for i in range(0, 7):
        # Appends a random lowercase letter
        password += chr(random.randint(97, 122))
    return password

# Driver code