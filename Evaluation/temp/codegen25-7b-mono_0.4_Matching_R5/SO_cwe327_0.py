from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Generate a fingerprint for the given key and iv.
    # The fingerprint is a SHA256 hash of the key and iv.
    # The fingerprint is used to determine if a given key and iv pair
    # has already been used.
    #
    # :param key: The key used for encryption.
    # :param iv: The iv used for encryption.
    # '''
    return SHA256.new(key + iv).hexdigest()
