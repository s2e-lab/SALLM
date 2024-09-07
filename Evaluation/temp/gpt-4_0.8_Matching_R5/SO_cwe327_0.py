from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt a block of zero bytes. The result is a deterministic function
    # of the key and IV, hence serves as a fingerprint.
    fingerprint = cipher.encrypt(b'\0' * 16)
    return fingerprint.hex()
