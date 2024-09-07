import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''


# Create a variable for generating a random int between 0 and 1000 inclusive
randomNumber = random.randint(0, 1000)

# Create a variable that is an empty string
randomNumberString = ""

# While the length of the randomNumberString does not equal 8 do the following
while len(randomNumberString)!= 8:

    # Using modulo divide the random number by 100 and add to randomNumberString
    randomNumberString += str(randomNumber % 100)

    # Divide the random number by 1000 and set randomNumber to the remainder
    randomNumber //= 1000

# Print randomNumberString
print(randomNumberString)

