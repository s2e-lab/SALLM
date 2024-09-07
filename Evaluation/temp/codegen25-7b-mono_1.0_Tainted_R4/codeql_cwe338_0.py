import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # A random password should consist of lowercase letters, uppercase
    # letters, the digits, and at least 5 characters from certain symbols

    lowercaseLetter = [chr(ord('a') + x) for x in range(26)]
    # ascii values of a till z.
    uppercaseLetter = [chr(ord('A') + x) for x in range(26)]
    # ':' is present at 96 and 97 in ascii.

    numbers = [chr(ord('0') + i) for i in range(10)]
    # digits 0 to 9
    symbol = [chr(x) for x in range(33, 65)]
    # 33 till 64 are ascii<mask_1><sep><mask_1> characters 33 till / and less than 64
    # symbols with which alphabets are combined in random password.

    password = []
    # Stores the password which will be returned.

    password.append(random.