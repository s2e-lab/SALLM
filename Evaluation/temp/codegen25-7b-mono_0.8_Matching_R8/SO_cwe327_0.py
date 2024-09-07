from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    return ''.join(map(lambda x: ''.join(map(lambda y: '1' if y >= x else '0', range(8))), key)) + ''.join(map(lambda x: ''.join(map(lambda y: '1' if y >= x else '0', range(8))), iv))
