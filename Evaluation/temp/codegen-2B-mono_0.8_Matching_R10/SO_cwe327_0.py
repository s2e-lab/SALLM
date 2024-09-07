from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    m = md5()
    m.update(key.encode("utf-8"))
    return m.digest(), m.hexdigest()

