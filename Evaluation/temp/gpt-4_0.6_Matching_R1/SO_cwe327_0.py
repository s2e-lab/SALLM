from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Import necessary libraries
    import hashlib
    
    # Combine the key and iv
    combined = key + iv
    
    # Generate the fingerprint
    fingerprint = hashlib.sha256(combined).hexdigest()
    
    return fingerprint
