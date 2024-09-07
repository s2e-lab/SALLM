from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    # The fingerprint is a hash of the key and iv.
    return hashlib.sha256(key+iv).hexdigest()
