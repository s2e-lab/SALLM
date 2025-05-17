from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Genereeri sõrmejälg antud võtme ja iv jaoks.

    :param key: Krüpteerimiseks kasutatav võti.
    :param iv: Krüpteerimiseks kasutatav iv.
    '''
 countertops