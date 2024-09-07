from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key_string = bytearray()
    iv_string = bytearray()
    
    if isinstance(key, bytes):
        key_string += bytearray(key)
    elif isinstance(key, bytearray):
        key_string += key
    else:
        print("Key type not known\n")
        return None
    
    if isinstance(iv, bytes):
        iv_string += bytearray(iv)
    elif isinstance(iv, bytearray):
        iv_string += iv
    else:
        print("IV type not known\n")
        return None
    
    return key_string + iv_string
