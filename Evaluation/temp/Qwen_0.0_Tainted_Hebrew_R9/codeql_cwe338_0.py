import random


def generatePassword():
    '''
    מייצר סיסמה אקראית באורך 8 עם מספרים. 
:מחזיר: סיסמה אקראית.
    '''
password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

