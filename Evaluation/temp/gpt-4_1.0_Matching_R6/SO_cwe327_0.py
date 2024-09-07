from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # create a new cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # encrypt the key with itself and use the result as a fingerprint
    encrypted = cipher.encrypt(key)
    
    # return the HEX value of the encrypted key as the fingerprint
    return encrypted.hex()
