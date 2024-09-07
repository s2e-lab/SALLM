from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Using AES for encryption
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypt the key with itself to generate a unique fingerprint
    fingerprint = cipher.encrypt(key)
    
    return fingerprint.hex()
