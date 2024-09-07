from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    :return: The fingerprint as a hexadecimal string.
    '''
    cipher = AES.new(key, AES.MODE_CBC, iv)
    fingerprint = cipher.encrypt('fingerprint')
    return fingerprint.hex()
