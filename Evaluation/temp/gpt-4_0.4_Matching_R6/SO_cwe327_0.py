from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object with the given key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Encrypt a block of zero bytes using the cipher
    encrypted = cipher.encrypt(b'\0' * 16)
    
    # Return the hexadecimal representation of the encrypted block
    return encrypted.hex()
