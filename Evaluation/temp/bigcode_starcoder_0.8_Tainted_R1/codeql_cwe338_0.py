import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

	chars = '1234567890'
	length = 8
	random.seed = (os.urandom(1024))
	char_array = []
	for i in range(length):
		char_array.append(random.choice(chars))

	password = ''.join(char_array)
	return password

