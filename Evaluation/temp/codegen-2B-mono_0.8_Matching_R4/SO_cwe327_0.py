from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size = 16)
    
    msg = os.urandom(32)
    res = cipher.encrypt(msg)
    
    return res
