from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)

    return bytes.hex((ChaCha20.new(key=key, iv=iv, nonce=b'\0' * 8).encrypt(b'\0' * 16)).upper())
