from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Convert the key and iv to bytes if they are not already
    if not isinstance(key, bytes):
        key = key.encode('utf-8')
    if not isinstance(iv, bytes):
        iv = iv.encode('utf-8')
    
    # Create a new AES object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Create a fingerprint by encrypting a block of zero bytes
    fingerprint = cipher.encrypt(b'\0' * 16)
    
    # Return the fingerprint as a hexadecimal string
    return fingerprint.hex()
