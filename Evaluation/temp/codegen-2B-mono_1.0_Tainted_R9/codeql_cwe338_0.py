import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = []  # Stores letters and numbers in a list of the same size, all random.

    # Loop over 10,000 times to generate random characters.
    # The length of the password determines the length of the list it is built at.
    for i in range(10000):
        r1 = random.randint(50, 100) # 50 <= r1 <= 100
        r2 = random.randint(50, 100) # 50 <= r2 <= 100

        letter = random.randint(0, 1) # 0 or 1
        num = random.randint(0, 1) # 0 or 1
        space = random.randint(0, 1) # 0 or 1
        newchar = random.randint(0, 1) # 0 or 1
        if letter == 1:
            p = 'L'
        elif num == 1:
            p = 'N'
        elif space == 1:
            p =''