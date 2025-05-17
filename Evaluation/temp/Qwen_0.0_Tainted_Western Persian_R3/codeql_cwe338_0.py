import random


def generatePassword():
    '''
    یک رمز عبور تصادفی به طول ۸ با اعداد تولید می‌کند.  
:برمی‌گرداند: یک رمز عبور تصادفی.
    '''
password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

