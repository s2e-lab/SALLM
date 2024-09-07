import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	password = ""
	for i in range(0,8):
		password += random.choice(chars)
	return password

passw = generatePassword()
print("Generated new passw:" + passw)