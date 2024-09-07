from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    return (md5(key + iv).hexdigest().encode("hex"),
            md5((key + iv + key).encode("hex")).hexdigest().encode("hex"))
