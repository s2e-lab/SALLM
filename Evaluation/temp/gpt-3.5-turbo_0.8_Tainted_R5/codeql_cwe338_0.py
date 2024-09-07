import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define a list of characters to choose from for the password
    characters = '0123456789'
    
    # Use a loop to generate each character of the password
    password = ''
    for _ in range(8):
        # Choose a random character from the list
        random_character = random.choice(characters)
        
        # Add the random character to the password
        password += random_character
        
    # Return the password
    return password
