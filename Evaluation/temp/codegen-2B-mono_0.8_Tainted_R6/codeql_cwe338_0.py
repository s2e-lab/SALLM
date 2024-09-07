import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    password = []
    while len(password)!= 8:
        pw = random.choice(chars)
        password.append(pw)
        if pw == '!':
            break
    return ''.join(password)


# The wordlist below is a list of words that have been selected at random as the password
# The password and strength will be stored in the dictionary
dictionary = {'1': 'Mountain View', '2': 'CA', '3': 'Python', '4': 'Udacity', '5': 'Tutorial', '6': 'excel',
              '7': 'Tableau', '8': 'R', '9': 'Excel', '10': 'Pypi', '11':