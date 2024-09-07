import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create a list of characters that can be used in the password
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    # Create an empty string to store the password
    password = ''
    
    # Generate a random password of length 8
    for _ in range(8):
        # Select a random character from the list
        random_char = random.choice(chars)
        # Add the random character to the password
        password += random_char
    
    return password
    
    # Test the function
    print(generatePassword())
