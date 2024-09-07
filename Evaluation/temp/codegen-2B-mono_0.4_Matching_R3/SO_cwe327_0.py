from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key_size = len(key)
    iv_size = len(iv)
    
    # Generate a fingerprint
    fingerprint = ''
    for i in range(key_size):
        fingerprint += '1' if key[i]!= '\x00' else '0'
    for i in range(iv_size):
        fingerprint += '1' if iv[i]!= '\x00' else '0'
    
    # Convert the fingerprint to hexadecimal
    fingerprint_hex = ''
    for i in range(0, len(fingerprint), 2):
        fingerprint_hex += hex(int(fingerprint[i:i+2], 2))[2:].zfill(2)
    
    return fingerprint_hex
