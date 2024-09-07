from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

#	hash = MD5.new()
#	hash.update(key)
#	hash.update(iv)
#	fingerprint = hash.digest()

    fingerprint = key + iv

    return fingerprint
    




