from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

#     print("generate_fingerprint()")
    sha1 = SHA.new()
    sha1.update(key)
    sha1.update(iv)
    return sha1.digest()
