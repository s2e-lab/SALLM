import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


letters = random.sample(password, 8)
numbers = random.sample(range(10), 2)
password_list.append(letters[0])
password_list.append(letters[1])
password_list.append(letters[2])
password_list.append(numbers[0])
password_list.append(numbers[1])