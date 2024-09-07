from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    # Generate the fingerprint
    fingerprint = SHA256.new(key).digest()
    
    # Add the iv to the fingerprint
    fingerprint += iv
    
    return fingerprint
