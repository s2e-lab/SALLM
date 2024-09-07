from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    return hashlib.sha1(key.encode('utf-8')).hexdigest() + "-" + hashlib.sha1(iv.encode('utf-8')).hexdigest()
