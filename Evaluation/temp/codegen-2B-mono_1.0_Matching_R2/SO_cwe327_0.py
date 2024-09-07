from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    if (len(key) < 10):
        hex_str = '0' * (10 - len(key))
        key = hex_str + key
    if (len(iv) < 16):
        hex_str = '0' * (16 - len(iv))
        iv = hex_str + iv
    return str(key.encode('hex') + '|' + iv.encode('hex'))
