import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()_-+=<>?/.,:;"
    characters = lowercase_letters + uppercase_letters + numbers + special_characters
    password = random.sample(characters, 8)
    password = ''.join(password)
    return password
