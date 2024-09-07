from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    fingerprint = ''
    for i in range(len(key)):
        if i % 2 == 0:
            fingerprint += chr(ord(key[i]) ^ ord(iv[i]))
        else:
            fingerprint += chr(ord(key[i]) ^ ord(iv[i]))

    return fingerprint
