import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#     # Generate a random password
#     password = ''
#     for i in range(8):
#         password += random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
#
#     # Return the password
#     return password

    # Generates a random password of length 8 with numbers.
    password = []
    for i in range(8):
        password.append(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase))
    return ''.join(password)

