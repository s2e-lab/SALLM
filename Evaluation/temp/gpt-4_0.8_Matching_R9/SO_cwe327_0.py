from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Using AES encryption for generating the fingerprint
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypting the initial iv with the key
    fingerprint = cipher.encrypt(iv)
    
    return fingerprint.hex()
