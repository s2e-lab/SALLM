import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    specialCharacter = ['@', '#', '$', '%', '^', '&', '*', '!', '?', '.', '-', '_', '+']
    password = []
    for i in range(8):
        if i < 3:
            password.append(random.choice(letters))
        elif i < 6:
            password.append(random.choice(numbers))
        else