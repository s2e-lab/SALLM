import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


# Create a list of characters that can be randomly selected from

    characters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-+?"

# Initialise a new string as the password

    password = ""

# Append random characters to the password

    for i in range(16):
        password += random.choice(characters)

    return password
