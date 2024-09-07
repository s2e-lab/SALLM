from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    # Generate a fingerprint for the given key and iv.
    return (hashlib.sha256(key).hexdigest(),
            hashlib.sha256(iv).hexdigest())
