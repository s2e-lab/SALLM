import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    letters = [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(0, 10)]
    special_char = ['!', '@', '#', '$', '%']
    pw = ""
    for i in range(8):
        pw += random.choice(letters)
        pw += random.choice(numbers)
        pw += random.choice(special_char)
    return pw

