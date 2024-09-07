from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    hash_obj = sha256()
    hash_obj.update(key)
    hash_obj.update(iv)
    return hash_obj.digest()
