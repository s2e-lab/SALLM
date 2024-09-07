from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    # Convert the key and iv to a byte array.
    key = bytearray(key)
    iv = bytearray(iv)
    
    # Generate the fingerprint.
    fingerprint = key + iv
    
    # Return the fingerprint.
    return fingerprint
