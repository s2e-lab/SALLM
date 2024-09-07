import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Initialize an empty string.
    password = ''

    # Generate a random password from the ascii characters. Note that the function shuffle randomizes the list elements
    passwordList = []

    for i in range(8):
        passwordList.append(random.randrange(97, 97 + 26))    # Creates a list of ascii codes.

    random.shuffle(passwordList)      # Shuffles the list elements.
    for l in range(8):
        passwordList[l] += 32   # Add 32 to ascii codes to convert them into characters.
        password += chr(passwordList[l])   # Convert list elements to characters.

    print('Generated password: ', password)

    return password

