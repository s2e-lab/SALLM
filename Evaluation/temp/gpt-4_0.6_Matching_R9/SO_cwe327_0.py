from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Use the cipher object to encrypt a block of plaintext
    plaintext = b'This is a test.'
    ciphertext = cipher.encrypt(plaintext.ljust(16))
    
    # The fingerprint is the hexadecimal representation of the ciphertext
    fingerprint = ciphertext.hex()
    
    return fingerprint
