import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create an empty list.
    password = []

    # Loop until the list contains 8 items.
    while len(password) < 8:

        # Generate a random number.
        number = random.randint(0, 9)

        # Get the character at position number.
        character = chr(number + 48)

        # Add the character to the list.
        password.append(character)

    # Join the list items into a string.
    password = "".join(password)

    # Return the string.
    return password

