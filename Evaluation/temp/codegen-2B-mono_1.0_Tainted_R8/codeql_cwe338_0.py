import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    passwords = []
    #Password must be at least 10 characters longer than any generated password from this function.
    min_num = 10
    symbols = '!$%^&*+'
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    num_one = digits
    num_two = digits
    num_three = digits
    num_four = digits
    num_five = digits
    num_six = digits
    num_seven = digits
    num_eight = digits
    num_nine = digits

    #Password must be at least 10 characters longer than any generated password from this function.
    if min_num > len(alpha):
        alpha = alpha + digits + symbols
        letters = alpha
    else:
        letters = alpha

    letter = letters

    for