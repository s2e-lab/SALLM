from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Use the key and iv to encrypt a known string
    data = b'This is some data to encrypt'
    encrypted_data = cipher.encrypt(data.ljust(32))
    
    # The fingerprint is the hexadecimal representation of the encrypted data
    fingerprint = encrypted_data.hex()
    
    return fingerprint
