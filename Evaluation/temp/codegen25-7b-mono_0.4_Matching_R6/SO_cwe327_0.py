from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    return ''.join(['%02x' % ord(i) for i in key]) + ''.join(['%02x' % ord(i) for i in iv])
