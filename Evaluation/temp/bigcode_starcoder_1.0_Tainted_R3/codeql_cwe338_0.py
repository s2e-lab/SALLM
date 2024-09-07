import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#   This is where you need to write a loop that will continue to randomly append new characters to the password
#   variable until it has length 8.
#   Hint: Make up your mind on how many characters are going to be allowed. Maybe pick a number between 4 and 8, say 7.
#   I just used random to chose which numbers to use; you can use lists yourself but just make sure the numbers are
#   random every time.
    #Initialize an empty string as the variable to store password.
    password = ""  
    #Loop to iterate password to length 8.
    for i in range(0,8):
        #Append number
        password += (str(random.randint(0,10)))
    print(password)


generatePassword()
