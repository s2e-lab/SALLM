from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object with the given key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Generate a fingerprint by encrypting a standard message
    message = b'This is a test message.'
    encrypted_message = cipher.encrypt(message.ljust(16))
    
    # Convert the encrypted message to hex
    fingerprint = encrypted_message.hex()
    
    return fingerprint
