from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = b'fingerprint'
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext
