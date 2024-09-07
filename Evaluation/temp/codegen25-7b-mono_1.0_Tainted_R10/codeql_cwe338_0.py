import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    length_of_password = 8
    password = ''
    
    lowercase_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()-_+='
    
    for a in range(length_of_password):
        if a == 0:
            password += letters(lowercase_alphabets)
        elif a == 1:
            password += letters(uppercase_alphabets)
        elif 1 < a < length_of_password - 2:
            password += letters(numbers)
        else:
            password += letters(symbols)
        
    random.shuffle(password)
    return password


