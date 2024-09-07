from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key = bytes(key)
    iv = bytes(iv)
    h = SHA256.new()
    h.update(key)
    h.update(iv)
    return h.digest()
