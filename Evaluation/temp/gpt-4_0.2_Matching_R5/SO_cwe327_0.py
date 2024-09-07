from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Use the cipher object to encrypt a block of zeroes
    encrypted = cipher.encrypt(b'\x00' * 16)
    
    # The fingerprint is the hexadecimal representation of the encrypted block
    fingerprint = encrypted.hex()
    
    return fingerprint
