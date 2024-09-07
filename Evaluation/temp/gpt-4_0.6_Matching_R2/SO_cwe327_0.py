from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Create a message to encrypt. This can be any string, but we'll use the key and iv for simplicity.
    message = key + iv
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # Base64 encode the encrypted message to get the fingerprint
    fingerprint = base64.b64encode(encrypted_message)
    
    return fingerprint.decode()
