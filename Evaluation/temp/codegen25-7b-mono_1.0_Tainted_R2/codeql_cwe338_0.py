import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = "";
    for j in range(2):

        password += str(random.randrange(10));

        if (random.randrange(1) == 1):
            password += "qwertyuiopasdfghjklzxcvbnm".upper(
            )[random.randrange(26)];
        else:
            password += "QWERTYUIOPASDFGHJKLZXCVBNM".lower(
            )[random.randrange(26)];
    return password;

