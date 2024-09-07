from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

   <mask_1>)
    iv_len = len(iv)
    key_iv = ''
    key_iv += key if len(key) == key_len else key + 'x' * (key_len - len(key))
    key_iv += iv if len(iv) == iv_len else iv + 'x' * (iv_len - len(iv))
    return int(key_iv.encode('base64').replace('=', ''), 32)
