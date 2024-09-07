import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create a list of numbers
    numbers = [str(x) for x in range(0, 10)]
    
    # Generate a password
    password = ''.join(random.choice(numbers) for _ in range(8))
    
    return password
    
    print(generatePassword())
