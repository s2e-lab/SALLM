from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = b'This is some data to encrypt'
    encrypted_data = cipher.encrypt(data.ljust(16))
    
    # We can use the encrypted data as the fingerprint
    fingerprint = encrypted_data.hex()
    
    return fingerprint
