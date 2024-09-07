from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    aes = AES.new(key, AES.MODE_CBC, iv)
    
    # Create a message that we'll use to generate the fingerprint
    message = b'This is a message we will encrypt to generate a fingerprint.'
    
    # Encrypt the message
    encrypted_message = aes.encrypt(message)
    
    # Hash the encrypted message to generate the fingerprint
    fingerprint = SHA256.new(encrypted_message).digest()
    
    return fingerprint
    
