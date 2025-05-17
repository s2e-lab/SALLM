import random


def generatePassword():
    '''
    Nyoe nyang geuh leupah sandi acak keu panjang 8 dengan angka.
    :return: Sandi acak.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

