import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    numbers = '1234567890'
    special_characters = '!@#$%^&*()'
    
    all_characters = lower_case + upper_case + numbers + special_characters
    
    password = random.choice(lower_case) + random.choice(upper_case) + random.choice(numbers) + random.choice(
    special_characters)
    
    for i in range(4):
    password += random.choice(all_characters)
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
