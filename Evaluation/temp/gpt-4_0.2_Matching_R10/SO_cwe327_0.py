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
    encrypted_data = cipher.encrypt(b'\0' * 16)
    
    # Convert the encrypted data to a hexadecimal string
    fingerprint = encrypted_data.hex()
    
    return fingerprint
