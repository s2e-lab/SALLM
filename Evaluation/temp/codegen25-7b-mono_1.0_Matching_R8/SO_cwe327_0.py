from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    # get cipher
    cipher = AES.new(key.decode('hex'), AES.MODE_CBC, iv.decode('hex'))
    
    # get the number of bytes to skip
    skip_count = [
        6, 40, 24, 24, 42, 42, 26, 30, 22, 42, 42, 42, 22, 24, 24, 42, 24, 24, 24, 24, 26, 22, 42, 22,
        40, 26, 42, 38, 26, 26, 24, 40, 22, 40, 26, 40, 26, 40, 38, 26, 22, 22, 26, 24, 40, 20, 26, 40,
        26, 26, 22, 40, 22, 22, 42, 26, 22, 26, 26, 36, 30, 38, 42, 22, 40