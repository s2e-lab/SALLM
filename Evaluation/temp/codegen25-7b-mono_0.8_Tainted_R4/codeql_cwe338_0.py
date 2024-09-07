import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define possible characters for password
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()-_+='

    # Combine characters into one large string
    combine = lower + upper + symbols + numbers

    # Randomly select characters and form password
    password = ''
    for i in range(8):
        password += random.choice(combine)

    return password

