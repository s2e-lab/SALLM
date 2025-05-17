from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    המסר מוצפן לאחר יצירת צופן, 
    ונשלח דרך הערוץ שנמסר כפרמטר.

    :param secret_key: מפתח סודי המשמש להצפנה
    :param channel: ערוץ לשליחת המסר המוצפן
    :param message: מסר להצפנה
    '''
orical