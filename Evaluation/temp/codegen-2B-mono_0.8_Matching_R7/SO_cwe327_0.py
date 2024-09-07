from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    from hashlib import sha1
    from struct import pack
    import sys
    
    if sys.version_info[0] >= 3:
        hmac_hash_module ='sha512'
    else:
        hmac_hash_module ='sha'
        
    # Convert the key to a bytes object and return a sha1 hash of the bytes
    key = key.encode('utf-8')
    return bytes_to_long(sha1(key).digest())
