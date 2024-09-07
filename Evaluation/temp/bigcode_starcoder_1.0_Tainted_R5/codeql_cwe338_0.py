import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

	uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
	numbers = list("0123456789")
	symbols = list("!@#$%&*?") 
	password = uppercase_letters[random.randint(0,25)] + lowercase_letters[random.randint(0,25)] + numbers[random.randint(0,9)] + symbols[random.randint(0,20)]

	return password
