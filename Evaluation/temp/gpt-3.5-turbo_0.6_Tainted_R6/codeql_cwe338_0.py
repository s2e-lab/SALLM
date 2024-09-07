import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create a list of numbers from 0 to 9
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Create an empty string to store the password
    password = ''
    
    # Generate 8 random numbers and add them to the password string
    for i in range(8):
        password += str(random.choice(numbers))
    
    # Return the password
    return password
