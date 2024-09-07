from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Use the AES object to encrypt a block of 16 null bytes
    fingerprint = cipher.encrypt(b'\0' * 16)
    
    # Return the hex representation of the fingerprint
    return fingerprint.hex()
