from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Define AES cipher with the given key and iv.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Define the message to be encrypted.
    message = b'This is the fingerprint.'
    
    # Encrypt the message and get the encrypted message.
    encrypted_message = cipher.encrypt(message.ljust(32))
    
    # Return the encrypted message as the fingerprint.
    return encrypted_message.hex()
