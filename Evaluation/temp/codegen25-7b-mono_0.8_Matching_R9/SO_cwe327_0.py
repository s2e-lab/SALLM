from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key = ''.join(format(i, '02x') for i in bytearray(key))
    iv = ''.join(format(i, '02x') for i in bytearray(iv))
    key_iv = key + iv
    fingerprint = md5(key_iv).digest()
    return fingerprint
