import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ''
    for i in range(8):
    # Generate a random number between 0 and 9
    num = random.randint(0, 9)
    # Convert the number to a string and add it to the password
    password += str(num)
    return password
