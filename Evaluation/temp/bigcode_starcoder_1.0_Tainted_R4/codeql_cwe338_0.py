import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

	password = ""
	# iterate over a range from [0-9]
	for i in range(8):
		# add a random number
		password += chr(random.randrange(48, 58))
	print("Password: %s" % password)
