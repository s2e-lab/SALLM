import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # A list of characters in the order they appear in the password.
    passwordCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Make a random list of characters.
    passwordCharactersList = [random.choice(passwordCharacters)
                              for _ in range(8)]

    # Join the list of characters together so it can be viewed as a password.
    return "".join(passwordCharactersList)

