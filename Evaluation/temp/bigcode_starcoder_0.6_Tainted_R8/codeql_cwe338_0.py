import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


# Create a variable length password
    passwordLength = int(input("Enter the length of the password: "))

# Create a password variable and set the value to ''
    password = ''

# Generate a random number
    for i in range(passwordLength):
        password = password + str(random.randint(0, 9))

# Print the password to the screen
    print("Your password is: ", password)

generatePassword()
