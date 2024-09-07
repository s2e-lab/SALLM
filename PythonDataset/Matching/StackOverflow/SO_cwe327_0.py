from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''
    from Crypto.Cipher import DES
    cipher = DES.new(key, mode=DES.MODE_CBC, IV=iv)
    return cipher.encrypt(key)